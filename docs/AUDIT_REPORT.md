# Audit report

## Scope and findings

Assembly inspected the three supplied attachments locally. No source data were downloaded, no estimator was fitted, and no notebook training/audit cells were executed. Selected configuration and aggregate relations were checked; complete numerical reproduction remains unavailable.

The package contains the original Word manuscript, notebook and ZIP with unchanged bytes, plus the original 20 extracted outputs. The publication manifest records pipeline v8, reporting v18 and the model signature `fe8bc39e393c2c1d`; notebook training evidence retains internal audit v15. Seed 42 applies to the model pipeline; seed 20261018 applies to the reporting audit. Sensitivity analyses use 14/30-day blocks with 300 requested resamples, in addition to the main 7-day/1,000 and calibration 7-day/600 settings.

| Item | Current evidence | Audit consequence |
|---|---|---|
| Original notebook | Present, hashed | Code can be inspected; historical execution not independently established |
| 10 PNG + 10 aggregate CSV | Present, hashed | Results can be traced at aggregate level |
| Four source SHA-256 values | Present in output manifest | Claims can be checked against source bytes after recovery; source bytes absent here |
| Fitted model bundle | Path and signature recorded, binary absent | Model identity cannot be independently checked here |
| Per-observation probabilities | Absent | AP/ROC-AUC/Brier cannot be independently recomputed here |
| 10 training-evidence CSVs | Absent | Recorded combined evidence hash cannot be reconstructed here |
| Original runtime lock and execution log | Absent | Exact historical numerical reproduction not established |
| Persistent code archive DOI | Not provided | Authors must create the archive and insert its actual DOI |

## Scientific limits retained

The supplied editorial gate file includes `NOT_READY` and `INCOMPLETE` decisions. Those decisions remain unchanged. The repeatedly used 2025 evaluation is exploratory. Report labels do not verify flood absence. Operational lead time, independent post-2025 validation, incomplete station identification and a current novelty assessment remain separate research issues. Packaging cannot resolve them.

This is a transparency package, not a certificate of SINTA-2 compliance, scientific impact or acceptance. No claim is made that a universal SINTA-2 repository specification has been met. Check the target journal's current policies separately.

## Verification boundary

`verify_package.py` checks file digests, exact copied ZIP members, configuration assignments using the AST, Table 3 identity, counts, selected score deltas and bootstrap/replicate settings. `provenance/assembly_verification.json` records the result. It does not validate raw station mapping, fitted model internals, probabilities, historical provenance, or full statistical correctness. Hashes establish a byte baseline and detect later changes; they do not establish truth or prevent deliberate replacement of both files and manifest. A tagged commit and archived DOI improve version traceability.
