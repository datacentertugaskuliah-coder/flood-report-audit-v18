# Output data dictionary

Generated from the actual supplied CSV headers. See notebook calculations for exact estimator definitions. Probability, AP, ROC-AUC, Brier, precision and recall columns use raw proportions/scores unless a header explicitly states percentage points. Region keys are source administrative identifiers, not coordinates.

## 01_input_integrity_manifest.csv

Rows: 31.

| Column | Observed example |
|---|---|
| `audit_check` | Original data DOI |
| `observed_value` | 10.17632/d7j3s64vvr.1 |
| `decision` | base dataset metadata reference; any user-supplied extension must be documented separately |

## 02_region_year_observation_quality.csv

Rows: 162.

| Column | Observed example |
|---|---|
| `region_key` | city_bandung |
| `year` | 2020 |
| `region_days` | 366 |
| `positive_region_days` | 8 |
| `mean_available_station_fraction_lag1` | 0.9945205479452056 |
| `lag1_no_station_days` | 0 |
| `lag1_coverage_below_half_days` | 0 |
| `recorded_positive_rate` | 0.02185792349726776 |
| `evaluation_period_role` | training |
| `data_quality_flag` | check |

## 03_region_test_quality_and_support.csv

Rows: 27.

| Column | Observed example |
|---|---|
| `region_key` | city_bandung |
| `test_region_days` | 365 |
| `test_positive_n` | 10 |
| `mean_lag1_station_coverage` | 1.0 |
| `zero_coverage_days` | 0 |
| `below_50pct_coverage_days` | 0 |
| `ap_reliability_flag` | descriptive_only |
| `brier_stress` | 0.026574930082753093 |
| `ap_stress` | 0.07406796661090378 |
| `brier_standard` | 0.026588492993890007 |
| `ap_standard` | 0.07011025130189763 |
| `brier_histgb` | 0.02652479001129388 |
| `ap_histgb` | 0.07075226118471281 |

## 04_frozen_test_model_metrics.csv

Rows: 9.

| Column | Observed example |
|---|---|
| `model` | Seasonal-region baseline |
| `test_n` | 9855 |
| `test_positive_n` | 296 |
| `prevalence` | 0.030035514967021816 |
| `mean_predicted_probability` | 0.026278069188361352 |
| `mean_probability_minus_observed_prevalence` | -0.003757445778660464 |
| `mean_probability_gap_percentage_points` | -0.3757445778660464 |
| `average_precision` | 0.06926795653886837 |
| `roc_auc` | 0.7247786153137131 |
| `brier_score` | 0.02860270232342481 |
| `brier_skill_vs_seasonal_baseline` | 0.0 |
| `calibration_intercept_descriptive` | 0.2564283805970664 |
| `calibration_slope_descriptive` | 1.0348258487156548 |
| `status` | exploratory_reused_2025_test |

## 05_paired_block_bootstrap_sensitivity.csv

Rows: 18.

| Column | Observed example |
|---|---|
| `comparison` | Stress vs standard |
| `model_a` | Stress-trained uncertainty–quality stacking |
| `model_b` | Standard stacking |
| `block_days` | 7 |
| `bootstrap_reps` | 1000 |
| `observed_delta_ap` | 0.0062967609529868684 |
| `ap_ci95_low` | -0.003773525311762948 |
| `ap_ci95_high` | 0.016380141240368993 |
| `ap_bonferroni_sensitivity_low` | -0.009979116810544138 |
| `ap_bonferroni_sensitivity_high` | 0.021226218130763575 |
| `observed_brier_improvement` | 0.0001563025338329548 |
| `brier_ci95_low` | 4.154277614387004e-05 |
| `brier_ci95_high` | 0.00027420156464498784 |
| `brier_bonferroni_sensitivity_low` | 1.1033626510602533e-05 |
| `brier_bonferroni_sensitivity_high` | 0.00034394382683704575 |
| `evaluation_status` | exploratory_reused_2025_test_non_circular_blocks |
| `bootstrap_method` | non-circular moving-block bootstrap |
| `multiplicity_adjustment_scope` | Bonferroni sensitivity across 4 contrasts x 3 block lengths |
| `outcome_target` | recorded_flood_day |
| `evaluation_period` | exploratory_2025 |

## 06_corrected_at_risk_report_onset.csv

Rows: 9.

| Column | Observed example |
|---|---|
| `model` | Seasonal-region baseline |
| `model_training_target` | recorded_flood_day |
| `original_report_day_ap` | 0.06926795653886837 |
| `onset_at_risk_ap` | 0.04834740629979781 |
| `onset_at_risk_roc_auc` | 0.7038957987200523 |
| `onset_at_risk_n` | 8286 |
| `onset_at_risk_positive_n` | 179 |
| `onset_at_risk_prevalence` | 0.02160270335505672 |
| `onset_at_risk_ap_lift` | 2.2380257463694115 |
| `onset_all_region_days_ap` | 0.032548478260224806 |
| `onset_all_region_days_n` | 9855 |
| `onset_all_region_days_positive_n` | 179 |
| `onset_all_region_days_prevalence` | 0.018163368848300356 |
| `legacy_v10_outcome_conditioned_ap_not_comparable` | 0.033702563155536255 |
| `legacy_v10_n` | 9738 |
| `prior_7d_ineligible_region_days` | 1569 |
| `prior_7d_ineligible_negatives` | 1452 |
| `positive_continuation_days` | 117 |
| `report_onset_is_hydrologically_verified` | False |
| `evaluation_status` | exploratory_at_risk_conditioned_sensitivity_not_independent_holdout |

## 07_daily_alert_capacity.csv

Rows: 27.

| Column | Observed example |
|---|---|
| `model` | Seasonal-region baseline |
| `regions_flagged_per_day` | 1 |
| `days` | 365 |
| `total_flags` | 365 |
| `recorded_positive_region_days_detected` | 31 |
| `false_alerts` | 334 |
| `precision` | 0.08493150684931507 |
| `recall` | 0.10472972972972973 |
| `lift_vs_prevalence` | 2.8277027027027026 |
| `fraction_of_regions_flagged_per_day` | 0.037037037037037035 |
| `status` | retrospective_capacity_sensitivity_not_operational_validation |

## 08_paired_missingness_robustness.csv

Rows: 24.

| Column | Observed example |
|---|---|
| `mechanism` | MCAR |
| `additional_missing_target_fraction` | 0.1 |
| `comparator` | Standard stacking |
| `replicates` | 100 |
| `delta_ap_mean` | -0.004213090929863762 |
| `delta_ap_q025_simulation` | -0.007042843146213027 |
| `delta_ap_q975_simulation` | -0.002372131989430792 |
| `ap_better_fraction` | 0.0 |
| `brier_improvement_mean` | 2.6817654294432718e-05 |
| `brier_q025_simulation` | 2.9829750647447294e-06 |
| `brier_q975_simulation` | 5.015237592791458e-05 |
| `brier_better_fraction` | 0.98 |
| `uncertainty_qualification` | simulation spread, not statistical confidence interval |

## 09_date_block_calibration_uncertainty.csv

Rows: 40.

| Column | Observed example |
|---|---|
| `model` | HistGradientBoosting |
| `bin` | 1 |
| `n` | 986 |
| `positives` | 5 |
| `mean_probability` | 0.007486953213668617 |
| `observed_report_fraction` | 0.005070993914807302 |
| `wilson95_low_naive_iid` | 0.0021679123974930993 |
| `wilson95_high_naive_iid` | 0.011815598494427666 |
| `interval_limitation` | iid Wilson; ignores temporal and spatial dependence |
| `date_block7_boot95_low` | 0.0009858575276863214 |
| `date_block7_boot95_high` | 0.009700447093889713 |
| `date_block7_boot_reps` | 600 |
| `bootstrap_limitation` | Non-circular 7-day moving-block bootstrap; fixed calibration bins; repeated 2025 test use |

## 10_editorial_evidence_gates.csv

Rows: 39.

| Column | Observed example |
|---|---|
| `evidence_gate` | Exact dataset version and source DOI |
| `decision` | PASS |
| `reason_or_result` | 10.17632/d7j3s64vvr.1 |

## Interpretation conventions

`observed_delta_ap` and `delta_ap_mean` use model A or stress AP minus comparator AP. Brier improvement uses comparator Brier minus model A or stress Brier, so positive means lower Brier error. CSV 05 confidence intervals come from date-block bootstrap; CSV 08 simulation quantiles describe missingness-replicate spread and are not population confidence intervals. `_naive_iid` columns ignore clustered dates and regions. `legacy_v10` onset columns are retained for audit and are not comparable to the corrected at-risk denominator. `ap_better_fraction` and `brier_better_fraction` are proportions, not percentages. `bootstrap_reps` records successful resamples where applicable; requested counts live in the configuration.
