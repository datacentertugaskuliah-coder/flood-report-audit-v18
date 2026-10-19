# Reproducibility and completion

## Three different operations

**Inspect supplied aggregates:** run `python scripts/verify_package.py`. This checks hashes, copied attachments, configuration, table identity and selected aggregate consistency. It cannot recompute metrics from absent probabilities.

**Recover the original record:** preserve the original Drive folder `/content/drive/MyDrive/Flood_Research_Mendeley_v1`. Export existing files before retraining. The notebook deliberately excludes caches and training evidence from its 20-file publication ZIP. The supplied ZIP is not the 10-CSV training-evidence cache expected by `audit_only`.

**Reconstruct a new run:** use `notebooks/flood_v18_original.ipynb` in Colab. The default `PIPELINE_MODE='retrain'` rebuilds evidence but may reuse a matching fitted cache because `FORCE_RETRAIN=False`. `FORCE_RETRAIN=True` forces fitting. Preserve `FAST_TEST=False` for final exports. Source acquisition may require manual workbooks through `SOURCE_OVERRIDE_DIR`. Keep all four source filenames and validate SHA-256 against `config/frozen_experiment.json`. A new execution is not proof of historical runtime or exact historical results.

## Export from the original run

Open `notebooks/flood_v18_with_archive_export.ipynb` or copy only its last two cells into the notebook that has the original Drive mounted. Do not run the entire notebook merely to export files that already exist. The last cell embeds the export utility and calls it against the known Drive project root. It creates `/content/flood_v18_supplemental_record.zip` and downloads it in Colab.

Alternatively, run:

```bash
python scripts/export_run_record.py --project-root /path/to/Flood_Research_Mendeley_v1 --output /path/outside/project/flood_v18_supplemental_record
```

The tool checks expected source hashes and the canonical 10-file evidence signature when available. It stops on mismatches. It copies the exact-named model binary without loading pickle/joblib objects and records its binary SHA-256. Its filename is not independent proof of model metadata. Missing files remain marked missing. Review `export_status.json` and `export_file_manifest.json`.

The export captures the current runtime, which can differ from the training runtime. The exported ZIP contains source files only if they actually exist and match recorded hashes; confirm redistribution attribution from the source dataset before release. If model/evidence attachments exceed GitHub's regular file limits, use appropriate release assets or a persistent data archive and retain their checksum/link in the repository.

## Complete the public record

Recover the fitted bundle; observation-level 2025 predictions; all 10 canonical training-evidence CSVs; source workbooks or exact retrieval/version/hash instructions; feature schema and thresholds (normally inside the bundle); actual runtime lock and run log. Add author-verified citation metadata and code licensing. Record the final commit, release tag and persistent archive DOI. Recompute AP, ROC-AUC and Brier from frozen predictions in an independent verification before claiming end-to-end reproducibility.

Do not load an untrusted joblib/pickle file. This export utility only copies bytes.
