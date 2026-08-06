# JACS TYK2 RBFE — OpenFF 2.3.0

## Purpose

This submission prepares a **relative binding free energy (RBFE)** benchmark for the JACS TYK2 system using **OpenFF 2.3.0** and NAGL AM1-BCC charges. This network serves as a **learning exercise and replicate run** to demonstrate reproducibility and run-to-run variation in alchemical calculations.

## Submission Details

- **Benchmark Set**: `jacs_set`
- **System**: `tyk2`
- **Protocol**: Relative Hybrid Topology Protocol (RBFE)
- **Force Field**: `openff-2.3.0`
- **Partial Charges**: `nagl_openff-gnn-am1bcc-1.0.0.pt`

## Deviations from Standard Workflow

See the [Standard Workflow](../../SUBMISSION_WORKFLOW.md)

- **Test scope** — Uses scope `Scope('openff', 'test', 'openff_2_3_0_tyk2')` rather than production campaign
- **Custom metadata script** — The metadata preparation script in `get_results/` is configured with this specific network key and parameters; update the `NETWORK_KEY` constant if re-running

## Files

- `create_network/plan_tyk2_rbfe.py` — Planning script adapted from `openfe-benchmarks` (modified to single TYK2 system)
- `create_network/log.txt` — Log output from planning script
- `get_results/_no_test_example_prepare_metadata.py` — Metadata preparation orchestrator
- `get_results/output/submission.yaml` — Submission metadata
- `get_results/output/zenodo_description.md` — Submission metadata
- `get_results/output/computational_results.json` — Results file
- `get_results/log.txt` — Log output from work-up script
- `alchemiscale_submission.ipynb` - Notebook for submitting alchemical networks to alchemiscale and monitoring their progress.
