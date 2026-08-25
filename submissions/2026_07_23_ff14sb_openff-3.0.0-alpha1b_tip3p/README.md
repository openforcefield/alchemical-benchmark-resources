
# FF14SB + OpenFF 3.0.0-alpha1b + TIP3P RBFE — Testing Hybrid Force Field

## Purpose

This submission tests **relative binding free energy (RBFE)** calculations using a **hybrid force field approach**: **FF14SB** for protein parameters combined with **OpenFF 3.0.0-alpha1b** for ligands and the **TIP3P water model**. This benchmark evaluates two specific JACS systems (tyk2, thrombin) using the standard RelativeHybridTopologyProtocol with this experimental force field combination.

## Submission Details

- **Benchmark Set**: `jacs_set`
- **Systems**: `tyk2` and `thrombin` (focused subset)
- **Protocol**: RelativeHybridTopologyProtocol (standard)
- **Protein Force Field**: `ff14sb` (AMBER)
- **Ligand Force Field**: `openff-3.0.0-alpha1b`
- **Water Model**: TIP3P
- **Solvation**: Neutral TIP3P with default ion neutralization
- **Status**: Submitted to OpenFE Benchmarks

### Completion Status

- **Phase 1: Network Creation** — Complete
  - Networks generated for tyk2 and thrombin systems
  - Validation passed; all transformations validated
  - Outputs in `outputs/alchemical_network_jacs_set_*.json`
- **Phase 2: Computation** — Complete
  - Ready for Alchemiscale submission via `alchemiscale_submission.ipynb`
- **Phase 3: Results & Metadata** — Complete
  - Will generate submission metadata after computation completes

## Deviations from Standard Workflow

- **Hybrid force field** — Uses FF14SB for protein (AMBER) and OpenFF 3.0.0-alpha1b for ligands (mixed force field)
- **Alpha force field component** — OpenFF 3.0.0-alpha1b is not a stable release; results exploratory
- **Standard protocol** — Uses standard RelativeHybridTopologyProtocol (not experimental Pontibus)
- **Focused systems** — Only tyk2 and thrombin, not full JACS set of 8 systems

## Files

- `plan_tyk2_thrombin_rbfe.py` — Planning script for RBFE network generation with hybrid force field
- `outputs/alchemical_network_jacs_set_tyk2.json` — Generated network for tyk2
- `outputs/alchemical_network_jacs_set_thrombin.json` — Generated network for thrombin
- `alchemiscale_submission.ipynb` — Notebook for Alchemiscale submission
- `log.txt` — Execution log from network generation

## References

- [SUBMISSION_WORKFLOW.md](../../SUBMISSION_WORKFLOW.md) — Complete workflow guide
- [OpenFE Benchmarks Submission Guide](https://github.com/OpenFreeEnergy/openfe-benchmarks#submitting-a-new-benchmark) — Metadata and submission requirements
- [OpenFE Benchmarks](https://github.com/OpenFreeEnergy/openfe-benchmarks)
- [Alchemiscale User Guide](https://docs.alchemiscale.org/en/stable/user_guide/index.html)

- Create a `submission.yml` and `zenodo_description.md` (save here) with `openfe_benchmarks` script `prepare_metadata_submission.py`
- Document protocol customizations or deviations in this README
- Include provenance and references in submission metadata
