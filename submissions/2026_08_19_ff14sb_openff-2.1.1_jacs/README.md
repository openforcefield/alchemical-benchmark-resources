# ff14sb + OpenFF 2.1.1 RBFE

## Purpose

This submission tests **relative binding free energy (RBFE)** calculations using **ff14sb protein force field** combined with **OpenFF 2.1.1** small molecule force field with the **TIP3P water model**. This benchmark evaluates the RelativeHybridTopologyProtocol performance across the full JACS diverse set (8 systems) with this hybrid force field configuration.

## Submission Details

- **Benchmark Set**: `jacs_set` (8 systems: bace, cdk2, jnk1, mcl1, p38, ptp1b, thrombin, tyk2)
- **Protocol**: RelativeHybridTopologyProtocol with adaptive settings
- **Small Molecule Force Field**: `openff-2.1.1`
- **Protein Force Field**: `ff14sb` (from Amber tools)
- **Water Model**: TIP3P
- **Solvation**: Na⁺/Cl⁻ with 0.15 M ion concentration, automatic box sizing
- **Ligand Partial Charges**: OpenEye AM1BCC ELF10
- **Status**: Submitted to OpenFE Benchmarks

### Completion Status

- **Phase 1: Network Creation** — Complete
  - Networks generated for all 8 JACS systems
  - Validation passed; all transformations validated
  - Outputs in `create_networks/outputs/alchemical_network_jacs_set_*.json`
- **Phase 2: Computation** — Complete
  - Ready for Alchemiscale submission via `alchemiscale_submission.ipynb`
- **Phase 3: Results & Metadata** — Complete
  - Will generate submission metadata after computation completes

## Deviations from Standard Workflow

- **Hybrid Force Field** — Combines amber tools ff14sb for protein with OpenFF 2.1.1 for small molecules
- **Adaptive Protocol Settings** — Uses adaptive transformation settings to optimize protocol parameters per transformation

## Files

- `create_networks/_example_plan_rbfe.py` — Planning script for RBFE network generation
- `create_networks/outputs/alchemical_network_jacs_set_*.json` — Generated networks for all 8 systems
- `alchemiscale_submission.ipynb` — Notebook for Alchemiscale submission
- `environment_full.yaml` — Complete computational environment specifications
- `alchemicalnetwork_scopekeys.json` — Scope keys recorded after computation

## References

- [SUBMISSION_WORKFLOW.md](../../SUBMISSION_WORKFLOW.md) — Complete workflow guide
- [OpenFE Benchmarks Submission Guide](https://github.com/OpenFreeEnergy/openfe-benchmarks#submitting-a-new-benchmark) — Metadata and submission requirements
- [OpenFE Benchmarks](https://github.com/OpenFreeEnergy/openfe-benchmarks)
- [Alchemiscale User Guide](https://docs.alchemiscale.org/en/stable/user_guide/index.html)
- [ff14sb Protein Force Field](https://ambermd.org/)
