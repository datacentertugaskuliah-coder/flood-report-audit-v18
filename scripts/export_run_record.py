#!/usr/bin/env python3
"""Ekspor berkas run yang benar-benar ada. Tidak melatih atau memuat model pickle."""
import argparse
import csv
import hashlib
import importlib.metadata
import json
import platform
import shutil
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

EXPECTED_EVIDENCE_SHA = '2a476134a9b27dcf28639574dcdd68b3b5580a951cd37763fe3e5a95706c1d72'
SOURCES = {
 'Data-Ch-Jabar-2020-2025.xlsx':'92a207057853ed063fa4548892e515ae7d160f582a4469cde20f268e4230c99f',
 'Dataset_Flood_2020-2025.xlsx':'a5265db438bac4bd49d4a27d5dedba2d8beca405c49a5644630f6292858f3c28',
 'Dataset_Rainfall_Floods_2020-2025.xlsx':'c873bf2fa9a503f599db803325137ccf6149532254550517323ac9e6c4ae1d89',
 'West_Java_Rainfall_Station_Metadata_Lengkap.xlsx':'15afa28cec99f00825f97e7b5915d1a5caff7d16eb84851fe2d3a616c694d89a'}
STEMS = {
 'station':'01_station_mapping_audit','quality':'02_region_year_quality',
 'panel':'03_lagged_feature_panel','split':'04_temporal_split_balance',
 'metrics':'05_model_metrics_validation_and_test','pred':'06_held_out_test_predictions',
 'calibration':'07_test_reliability_bins','robustness':'08_station_missingness_robustness',
 'alerts':'09_operational_alert_budgets','bootstrap':'10_paired_block_bootstrap'}

def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda:stream.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()

def export(project_root, output):
    root=Path(project_root).expanduser().resolve();out=Path(output).expanduser().resolve()
    if not root.is_dir(): raise ValueError('Project root does not exist; mount the original Drive first.')
    if out.exists() or out.with_suffix('.zip').exists(): raise ValueError('Output path or ZIP already exists; choose a new destination.')
    if out==root or out.is_relative_to(root) or root.is_relative_to(out):
        raise ValueError('Use an output directory outside the source project tree.')
    records=[]; missing=[]; todo=[]
    for name,expected in SOURCES.items():
        p=root/'source'/name
        if not p.is_file():missing.append('source/'+name);continue
        actual=sha(p)
        if actual!=expected:raise ValueError('Source hash mismatch: '+name+'; preserve as a separate new run.')
        todo.append((p,'data/source/'+name))
    evidence={key:root/'v15_training_evidence_cache'/(stem+'.csv') for key,stem in STEMS.items()}
    # Jangan mengekspor potongan cache seolah-olah satu set lengkap.
    if all(p.is_file() for p in evidence.values()):
        combined=hashlib.sha256(''.join(sha(evidence[key]) for key in sorted(evidence)).encode()).hexdigest()
        if combined!=EXPECTED_EVIDENCE_SHA:
            raise ValueError('Training evidence signature differs from the supplied historical record; export this new run separately.')
        todo += [(p,'training_evidence/'+p.name) for p in evidence.values()]
        evidence_state='all ten files match recorded historical combined SHA-256'
    else:
        missing += ['training_evidence/'+p.name for p in evidence.values() if not p.is_file()]
        evidence_state='incomplete; no partial evidence set copied'
    bundle=root/'cache'/'frozen_model_bundle_fe8bc39e393c2c1d.joblib'
    if bundle.is_file():todo.append((bundle,'artifacts/'+bundle.name))
    else:missing.append('artifacts/'+bundle.name)
    out.mkdir(parents=True)
    for original,relative in todo:
        dest=out/relative;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(original,dest)
        records.append({'path':relative,'sha256':sha(dest),'size_bytes':dest.stat().st_size})
    environment=out/'environment';environment.mkdir()
    pins=sorted(set(f"{d.metadata['Name']}=={d.version}" for d in importlib.metadata.distributions() if d.metadata.get('Name')))
    (environment/'requirements-captured.txt').write_text('\n'.join(pins)+'\n')
    runtime={'captured_at_utc':datetime.now(timezone.utc).isoformat(),'python':sys.version,
             'platform':platform.platform(),'historical_runtime_verified':False,
             'qualification':'Current runtime at capture; does not prove original training environment.'}
    (environment/'runtime-captured.json').write_text(json.dumps(runtime,indent=2)+'\n')
    status={'missing':missing,'training_evidence':evidence_state,
            'model_bundle_copied':bundle.is_file(),'model_metadata_independently_verified':False,
            'qualification':'Binary copied without unpickling; filename alone does not authenticate its internal signature.',
            'historical_runtime_verified':False,'end_to_end_reproduction_verified':False,
            'source_data_attribution':'Preserve original dataset creators, DOI 10.17632/d7j3s64vvr.1, and CC BY 4.0 attribution.'}
    (out/'export_status.json').write_text(json.dumps(status,indent=2)+'\n')
    # Manifest mencakup environment/status juga; manifest tidak menghash dirinya sendiri.
    records=[{'path':str(p.relative_to(out)),'sha256':sha(p),'size_bytes':p.stat().st_size}
             for p in sorted(out.rglob('*')) if p.is_file()]
    (out/'export_file_manifest.json').write_text(json.dumps(records,indent=2)+'\n')
    archive=out.with_suffix('.zip')
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(out.rglob('*')):
            if p.is_file():z.write(p,str(Path(out.name)/p.relative_to(out)))
    print(json.dumps({'archive':str(archive),'missing_count':len(missing),'status':status},indent=2))
    return archive

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project-root',required=True);parser.add_argument('--output',required=True)
    args=parser.parse_args()
    export(args.project_root,args.output)
