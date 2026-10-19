# Training evidence missing

The required canonical 10 CSV are distinct from `research_outputs/`:

01_station_mapping_audit.csv
02_region_year_quality.csv
03_lagged_feature_panel.csv
04_temporal_split_balance.csv
05_model_metrics_validation_and_test.csv
06_held_out_test_predictions.csv
07_test_reliability_bins.csv
08_station_missingness_robustness.csv
09_operational_alert_budgets.csv
10_paired_block_bootstrap.csv

Expected original location: `v15_training_evidence_cache` in the Drive project root. The model-level CSV 06 contains per-observation probabilities; research output CSV 04 contains aggregate scores only. They are not interchangeable.
