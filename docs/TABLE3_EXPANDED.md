# Expanded Table 3: frozen experiment identity and resampling settings

| Record | Value | Evidence |
|---|---|---|
| Reporting notebook | v18; reporting audit `v18.0-teknika-sinta2-execution-guardrails` | Notebook reporting configuration and output manifest |
| Embedded training evidence audit | `v15.0-locked-temporal-prospective-validation-audit` | `EVIDENCE_AUDIT_VERSION` |
| Model pipeline | `v8.0.0-locked-temporal-missingness-prospective-audit-20261018` | Notebook and output manifest |
| Recorded model signature | `fe8bc39e393c2c1d` | Output manifest; fitted bundle not supplied |
| Feature version | `lagged-region-rainfall-v3` | Notebook and output manifest |
| Model pipeline seed | 42 | `SEED` |
| Reporting audit seed | 20261018 | `RANDOM_SEED`; downstream routines may derive offsets |
| Missingness replicates | 100 per mechanism and nonzero severity | Configuration and robustness summary |
| Missingness target levels | 0%, 10%, 20%, 30%; 0% denotes original inputs | `MISSING_LEVELS` |
| Primary bootstrap | 1,000 requested replicates; seven-day date blocks | Primary reporting configuration and CSV 05 |
| Sensitivity bootstrap | 300 requested replicates each; 14- and 30-day date blocks | Reporting configuration and CSV 05 |
| Calibration bootstrap | 600 requested replicates; seven-day date blocks | Reporting configuration and CSV 09 |
| Block implementation | Non-circular chronological blocks; sampled dates retain regional clusters | `sample_non_circular_blocks` |
| Temporal partitions | Train 2020–2023; calibration/thresholds 2024; exploratory evaluation 2025 | Notebook and manuscript |

Table 3 in the supplied manuscript omits the reporting audit seed and bootstrap sensitivity settings. Its version layers describe different components rather than one uniform software version. “Random seed: 42” alone does not describe every stochastic audit routine. This expanded table supplements the unchanged manuscript; authors can incorporate it within the journal page limit.

The 16-character model signature is a pipeline-generated identifier, not a SHA-256 checksum of the model binary. Source workbook hashes, training evidence signature and package file hashes are separate identifiers with different scopes.
