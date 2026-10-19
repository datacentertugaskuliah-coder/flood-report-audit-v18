#!/usr/bin/env python3
"""Regenerate the byte baseline only after reviewing intentional changes."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EXCLUDED={'provenance/file_manifest.json','provenance/assembly_verification.json'}
def files():
    for p in sorted(ROOT.rglob('*')):
        if not p.is_file():continue
        rel=p.relative_to(ROOT)
        if any(x in {'.git','__pycache__','.ipynb_checkpoints','.venv'} for x in rel.parts):continue
        if str(rel) in EXCLUDED or rel.name in {'.DS_Store','Thumbs.db'}:continue
        yield p
if __name__=='__main__':
    records=[{'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
              'size_bytes':p.stat().st_size} for p in files()]
    (ROOT/'provenance/file_manifest.json').write_text(json.dumps(records,indent=2)+'\n')
    print('Baseline files:',len(records))
