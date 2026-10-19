#!/usr/bin/env python3
"""Check supplied configuration and aggregates, not full model reproduction."""
import ast,csv,hashlib,json,math,sys,zipfile
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(name):return list(csv.DictReader((ROOT/'research_outputs'/name).open(encoding='utf-8-sig')))
def check(condition,message):
    if not condition:raise AssertionError(message)

def verify():
    records=json.loads((ROOT/'provenance/file_manifest.json').read_text())
    for record in records:
        p=ROOT/record['path'];check(p.is_file(),'Missing file: '+record['path'])
        check(sha(p)==record['sha256'],'Hash mismatch: '+record['path'])
    originals=json.loads((ROOT/'provenance/original_attachment_hashes.json').read_text())
    for path,digest in originals.items():check(sha(ROOT/path)==digest,'Original changed: '+path)
    with zipfile.ZipFile(ROOT/'provenance/original_10_PNG_10_CSV.zip') as z:
        for member in z.namelist():check(z.read(member)==(ROOT/member).read_bytes(),'Extracted output changed: '+member)
    output=ROOT/'research_outputs'
    check(len(list(output.glob('*.csv')))==10,'CSV count');check(len(list(output.glob('*.png')))==10,'PNG count')
    cfg=json.loads((ROOT/'config/frozen_experiment.json').read_text())
    nb=json.loads((ROOT/'notebooks/flood_v18_original.ipynb').read_text())
    code='\n'.join(''.join(c['source']) for c in nb['cells'] if c['cell_type']=='code')
    tree=ast.parse(code);assignments={}
    for node in tree.body:
        if isinstance(node,ast.Assign):
            for target in node.targets:
                if isinstance(target,ast.Name):assignments[target.id]=node.value
    expected={'SEED':42,'RANDOM_SEED':20261018,'BOOTSTRAP_REPS':1000,'ROBUSTNESS_REPS':100,'BLOCK_LENGTH_DAYS':7,
              'FAST_TEST':False,'PIPELINE_VERSION':cfg['pipeline_version'],
              'EVIDENCE_AUDIT_VERSION':cfg['embedded_evidence_audit_version'],
              'FEATURE_ENGINEERING_VERSION':cfg['feature_version']}
    for name,value in expected.items():check(ast.literal_eval(assignments[name])==value,'Notebook assignment: '+name)
    for name,value in [('N_BOOT_PRIMARY',1000),('N_BOOT_SENSITIVITY',300),('N_CALIBRATION_BOOT',600)]:
        node=assignments[name];check(isinstance(node,ast.IfExp) and isinstance(node.test,ast.UnaryOp) and isinstance(node.test.op,ast.Not) and isinstance(node.test.operand,ast.Name) and node.test.operand.id=='FAST_TEST','Bootstrap expression')
        check(ast.literal_eval(node.body)==value,'Full-mode bootstrap: '+name)
    integrity={x['audit_check']:x['observed_value'] for x in rows('01_input_integrity_manifest.csv')}
    for name,val in [('Model signature',cfg['recorded_model_signature']),('Random seed','42'),
                     ('Primary date-block bootstrap repetitions','1000'),('Calibration date-block bootstrap repetitions','600')]:
        check(integrity[name]==val,'Output manifest: '+name)
    metrics=rows('04_frozen_test_model_metrics.csv');check(len(metrics)==9,'Model count')
    scores={x['model']:x for x in metrics}
    onset={x['model']:x for x in rows('06_corrected_at_risk_report_onset.csv')}
    for x in metrics:check(int(x['test_n'])==9855 and int(x['test_positive_n'])==296,'Test support')
    for row in rows('05_paired_block_bootstrap_sensitivity.csv'):
        if row['outcome_target']=='recorded_flood_day':
            a=scores[row['model_a']];b=scores[row['model_b']]
            check(math.isclose(float(row['observed_delta_ap']),float(a['average_precision'])-float(b['average_precision']),abs_tol=1e-12),'AP delta')
            check(math.isclose(float(row['observed_brier_improvement']),float(b['brier_score'])-float(a['brier_score']),abs_tol=1e-12),'Brier delta')
        else:
            a=onset[row['model_a']];b=onset[row['model_b']]
            check(math.isclose(float(row['observed_delta_ap']),float(a['onset_at_risk_ap'])-float(b['onset_at_risk_ap']),abs_tol=1e-12),'At-risk onset AP delta')
        check(int(row['bootstrap_reps'])==(1000 if int(row['block_days'])==7 else 300),'Bootstrap replicate count')
    for row in rows('08_paired_missingness_robustness.csv'):check(int(row['replicates'])==100,'Missingness replicates')
    for row in rows('09_date_block_calibration_uncertainty.csv'):
        check(int(row['date_block7_boot_reps'])<=600,'Calibration repeats above requested count')
    # Inspect original Word Table 3 without modifying or rendering the manuscript.
    import xml.etree.ElementTree as ET
    ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    with zipfile.ZipFile(ROOT/'manuscript/Manuskrip_Teknika_10_Halaman_original.docx') as z:
        doc=ET.fromstring(z.read('word/document.xml'))
    table3=None
    for table in doc.findall('.//w:tbl',ns):
        parsed=[
            [''.join(t.text or '' for t in cell.findall('.//w:t',ns)) for cell in row.findall('w:tc',ns)]
            for row in table.findall('w:tr',ns)]
        if any('Audit version' in row for row in parsed):table3=dict(parsed[1:])
    check(table3 is not None,'Table 3 not found')
    check(table3['Model signature']==cfg['recorded_model_signature'],'Table3 signature')
    check(table3['Random seed']=='42','Table3 seed')
    return {'checked_files':len(records),'publication_png':10,'publication_csv':10,
            'status':'PASS_WITH_DOCUMENTED_MISSING_ARTIFACTS',
            'checks':['SHA-256 baseline','original attachment digests','original ZIP member byte equality','notebook configuration','Table 3 signature and seed','aggregate AP/Brier differences','bootstrap and simulation counts'],
            'not_verified':['raw data','fitted model internals','observation probabilities','original runtime','independent end-to-end numerical reproduction']}
if __name__=='__main__':
    try:result=verify()
    except Exception as exc:
        print('FAIL:',exc);sys.exit(1)
    result['checked_at_utc']=datetime.now(timezone.utc).isoformat()
    (ROOT/'provenance/assembly_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
