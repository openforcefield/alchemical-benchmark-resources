# FreeSolv ASFE — OpenFF 2.3.0

## Purpose

This submission prepares an **absolute solvation free energy (ASFE)** benchmark for the FreeSolv database using **OpenFF 2.3.0** and NAGL AM1-BCC charges. This network benchmark tests solvation thermodynamics calculations using the Absolute Solvation Protocol across 603 small molecules.

## Submission Details

- **Benchmark Set**: `solvation_set` (FreeSolv database)
- **System**: `freesolv`
- **Protocol**: Absolute Solvation Protocol (ASFE)
- **Force Field**: `openff-2.3.0`
- **Partial Charges**: `nagl_openff-gnn-am1bcc-1.0.0.pt`
- **Network**: `solvation_set/freesolv`
- **Transformations**: 603 solvation free energy calculations

## Workflow

**For detailed step-by-step instructions on the complete submission workflow**, see [SUBMISSION_WORKFLOW.md](../../SUBMISSION_WORKFLOW.md) in the repository root.

This submission follows the standard three-phase workflow:
1. **Network Creation** — Generate alchemical network from `plan_asfe_freesolv.py`
2. **Computation** — Submit to Alchemiscale using `alchemiscale_submission.ipynb`
3. **Results & Metadata** — Gather results and prepare metadata (see workflow guide)

## Deviations from Standard Workflow

None. This submission follows the standard workflow without modifications.

## Files

- `plan_asfe_freesolv.py` — Planning script from `openfe-benchmarks`
- `network_solvation_set_freesolv_asfe.json` — Generated network definition (603 transformations)
- `alchemiscale_submission.ipynb` — Jupyter notebook for Alchemiscale submission
- `submission.yaml` — Submission metadata
- `alchemicalnetwork_scopekey.txt` — Alchemiscale scope key(s) for this network

## Protocol Details

| Parameter | Value |
|-----------|-------|
| Vacuum Production Time | 2.0 ns |
| Vacuum Equilibration Time | 0.5 ns |
| Solvent Production Time | 10.0 ns |
| Solvent Equilibration Time | 1.0 ns |
| Timestep | 4.0 fs |
| Temperature | 298.15 K |
| Pressure | 1 bar |
| Lambda Schedule | lambda_elec:14, lambda_vdw:14, lambda_restraints:14 |

## Important Notes

- **Large benchmark**: 603 transformations will require significant compute time
- **Network composition**: Single largest system is 44 atoms; all transformations have 1 repeat

## References

- [SUBMISSION_WORKFLOW.md](../../SUBMISSION_WORKFLOW.md) — Complete workflow guide
- [OpenFE Benchmarks Submission Guide](https://github.com/OpenFreeEnergy/openfe-benchmarks#submitting-a-new-benchmark) — Metadata and submission requirements
- [OpenFE Benchmarks](https://github.com/OpenFreeEnergy/openfe-benchmarks)
- [Alchemiscale User Guide](https://docs.alchemiscale.org/en/stable/user_guide/index.html)
- [FreeSolv Database](https://freesolv.org/)

- [FreeSolv Database](http://www.freesolv.org/)
- [OpenFE Documentation](https://docs.openfree.org/)
- [Alchemiscale User Guide](https://docs.alchemiscale.org/en/stable/user_guide/index.html)

## Notes

This submission was prepared from archived Alchemiscale workflow data and represents a complete, validated alchemical network ready for benchmark evaluation.