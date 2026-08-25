
# OpenFF 3.0.0-alpha1b + OPC3 RBFE

## Purpose

This submission tests **relative binding free energy (RBFE)** calculations using an **alphab version** of OpenFF 3.0.0-alpha1b with the **OPC3 water model**. This benchmark compares the Pontibus protocol performance across the full JACS diverse set (8 systems) with this experimental force field configuration.

## Submission Details

- **Benchmark Set**: `jacs_set` (8 systems: bace, cdk2, jnk1, mcl1, p38, ptp1b, thrombin, tyk2)
- **Protocol**: Pontibus HybridTopProtocol (experimental)
- **Force Field**: `openff-3.0.0-alpha1b`
- **Water Model**: OPC3
- **Solvation**: Na⁺/Cl⁻ with 0.15 M ion concentration, automatic box sizing
- **Status**: Submitted to OpenFE-Benchmarks

### Completion Status

- **Phase 1: Network Creation** — Complete
  - Networks generated for all 8 JACS systems
  - Validation passed; all transformations validated
  - Outputs in `outputs/alchemical_network_jacs_set_*.json`
- **Phase 2: Computation** — Complete
  - Ready for Alchemiscale submission via `alchemiscale_submission.ipynb`
- **Phase 3: Results & Metadata** — Pending
  - Will generate submission metadata after computation completes

## Deviations from Standard Workflow

- **Pontibus Protocol** — Uses experimental Pontibus HybridTopProtocol instead of standard RelativeHybridTopologyProtocol
- **Alpha force field** — OpenFF 3.0.0-alpha1b is not a stable release; results should be considered exploratory

## Files

- `plan_rbfe_pontibus.py` — Planning script for RBFE network generation with Pontibus protocol
- `outputs/alchemical_network_jacs_set_*.json` — Generated networks for all 8 systems
- `alchemiscale_submission.ipynb` — Notebook for Alchemiscale submission
- `log.txt` — Execution log from network generation
- `alchemicalnetwork_scopekeys.json` — Scope keys will be recorded here after computation

## References

- [SUBMISSION_WORKFLOW.md](../../SUBMISSION_WORKFLOW.md) — Complete workflow guide
- [OpenFE Benchmarks](https://github.com/OpenFreeEnergy/openfe-benchmarks)
- [Alchemiscale User Guide](https://docs.alchemiscale.org/en/stable/user_guide/index.html)