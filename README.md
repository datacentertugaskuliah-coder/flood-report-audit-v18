# Flood report prediction: v18 audit package

This package links the supplied manuscript, unchanged v18 notebook, 10 figures, 10 aggregate CSV tables, frozen experiment record, provenance hashes, validation script, and a supplemental export tool.

**Status: aggregate audit only.** The supplied attachments do not contain the original source workbooks, fitted bundle, observation-level probabilities, 10 training-evidence CSVs, or original runtime lock. No models were retrained and no missing evidence was fabricated during assembly. Original reported values remain unchanged. Passing package checks does not establish independent reproducibility, validity, journal compliance, novelty, or acceptance.

## Start here

1. Read `docs/PANDUAN_GITHUB_DESKTOP.md` for Indonesian upload instructions.
2. Read `docs/AUDIT_REPORT.md` and `docs/TABLE3_EXPANDED.md` for findings and version/seed details.
3. Run `python scripts/verify_package.py` from the repository root. This uses the Python standard library only.
4. To complete the record, export existing files from the original Google Drive run with `scripts/export_run_record.py`. Follow `docs/REPRODUCIBILITY.md` before rerunning anything.

## Contents

| Path | Purpose |
|---|---|
| `manuscript/` | Original supplied Word manuscript, unchanged |
| `notebooks/flood_v18_original.ipynb` | Original supplied computational notebook, unchanged |
| `notebooks/flood_v18_with_archive_export.ipynb` | Same notebook plus optional archival export cells; no research logic changed |
| `research_outputs/` | Original 10 PNG + 10 CSV, extracted without modification |
| `config/frozen_experiment.json` | Explicit version layers, seeds, resampling, and recorded signatures |
| `provenance/file_manifest.json` | Independently computed SHA-256 of packaged files |
| `provenance/original_10_PNG_10_CSV.zip` | Original uploaded results ZIP |
| `docs/` | Audit, data dictionary, provenance and Desktop instructions |
| `scripts/` | Integrity checks and supplemental original-run export |
| `environment/requirements.in` | Dependency names inferred from notebook, not the original version lock |
| `artifacts/`, `training_evidence/`, `data/source/` | Documented missing items, not fabricated substitutes |

## Scientific interpretation

Training uses 2020–2023; calibration/threshold choice uses 2024. The repeatedly inspected 2025 period is exploratory. The target is recorded flood reporting, not hydrologically verified occurrence. Underreporting, station mapping, issuance-time availability, and independent validation remain unresolved. Better Brier performance does not demonstrate universal AP robustness under missingness. Preserve the original editorial gate decisions.

## Versioning and citation

Suggested initial tag: `v18-audit-package-1`. This is a packaging tag, not a new scientific experiment version. Add verified authors, repository URL, release commit and persistent archive DOI only after creation. The source dataset DOI is https://doi.org/10.17632/d7j3s64vvr.1 and must not be used as the DOI of this code package.

## Rights

See `RIGHTS.md`. This assembly does not assign a new code license or imply that the dataset license automatically licenses the code or manuscript.
