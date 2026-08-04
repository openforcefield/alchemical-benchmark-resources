# alchemical-benchmark-resources

This repository provides utilities, example scripts and resources for preparing alchemical benchmark submissions to the OpenFE "openfe-benchmarks" repository for training and posterity within OpenFF.

## Purpose

- Provide reproducible tooling and examples for creating or recycling alchemical networks.
- Store submission-ready directories that match the naming and metadata conventions used by openfe-benchmarks.
- Offer example scripts that can be used as input for generating networks and submission artifacts.
- Manage alchemiscale compute (separate from OpenFE)

## Getting started with Alchemiscale

- For installation of a compatible conda environment for this instance, please follow these instructions: [Alchemiscale deployment README](https://github.com/OpenFreeEnergy/alchemiscale.org-deployment/blob/main/deployments/root/README.md)
- Please see the User Guide for how to get started with usage: [Alchemiscale User Guide](https://docs.alchemiscale.org/en/stable/user_guide/index.html)
- You can also find a tutorial demo here: [Alchemiscale Demo tutorial](https://docs.alchemiscale.org/en/stable/tutorials/demo/Alchemiscale%20Demo.html)

## Submissions directory — required layout and metadata

Place each submission in `submissions/<directory-name>/`. The directory name should be descriptive and typically follows the pattern `YYYY_MM_DD_<force-field>_<system>` (e.g., `2026_03_17_openff-2.3.0_jacs_tyk2`). Each submission **must** contain a YAML metadata file named `submission.yaml`.

### Start here: Complete Workflow Guide

**New to submissions?** Start with [SUBMISSION_WORKFLOW.md](SUBMISSION_WORKFLOW.md), which provides:
- Step-by-step guidance through all three submission phases (network creation, computation, results gathering)
- Working examples from the `2026_03_17_openff-2.3.0_jacs_tyk2` submission
- Troubleshooting for common issues
- Reproducible workflow patterns

### Metadata & Submission Requirements

For complete documentation on `submission.yaml` fields, requirements, and examples, refer to the [openfe-benchmarks submission guide](https://github.com/OpenFreeEnergy/openfe-benchmarks#submitting-a-new-benchmark).

### Supporting Files

Each submission directory should contain:
- `submission.yaml` — metadata file (required)
- `README.md` — description of the submission and any workflow deviations
- `create_network/` — planning script and generated network JSON
- `get_results/` — metadata preparation script and output artifacts
- `alchemiscale_submission.ipynb` — Jupyter notebook for computation submission (if using Alchemiscale)

## Examples and recommended scripts

- Refer to `openfe-benchmarks` example scripts (for canonical workflow examples) by setting `script` to the example script path, e.g. `openfe-benchmarks/scripts/_example_rdfe.py`.

## Quick Reference: Three-Phase Workflow

| Phase | Purpose | Input | Output | Key Files |
|-------|---------|-------|--------|-----------|
| **1. Network Creation** | Design and generate alchemical transformations | Benchmark system definition | JSON network file | `create_network/plan_*.py`<br/>`alchemical_network_*.json` |
| **2. Computation** | Run calculations on Alchemiscale infrastructure | Network JSON + Scope | Completed jobs + results | `alchemiscale_submission.ipynb`<br/>Alchemiscale jobs |
| **3. Results & Metadata** | Gather results and prepare for archive | Network key + computed results | Submission artifacts | `get_results/output/`<br/>`submission.yaml` |

**See [SUBMISSION_WORKFLOW.md](SUBMISSION_WORKFLOW.md) for detailed step-by-step guidance.**

## Checklist before creating a pull request

Follow this checklist systematically before submitting your submission as a pull request. For detailed workflow guidance, see [SUBMISSION_WORKFLOW.md](SUBMISSION_WORKFLOW.md). For submission metadata requirements, see the [openfe-benchmarks submission guide](https://github.com/OpenFreeEnergy/openfe-benchmarks#submitting-a-new-benchmark).

### Network Creation & Validation

- [ ] Network generation script is included in `submissions/<directory>/create_network/`
- [ ] Network JSON file exists and is valid JSON (e.g., `alchemical_network_jacs_set_tyk2.json`)
- [ ] Network file generates without errors: `python create_network/plan_*.py`
- [ ] All molecular components are properly parameterized
- [ ] Network file size is reasonable for the transformation count

### Computation & Results

- [ ] Alchemiscale submission completed successfully (all jobs finished)
- [ ] Network archive exists: `AlchemicalNetwork-<gufe-hash>.json.bz2`
- [ ] Results file generated: `computational_results.json` with expected data
- [ ] Scope key(s) documented: `alchemicalnetwork_scopekeys.txt`
- [ ] Log files preserved: `get_results/log.txt`

### Metadata & Documentation

- [ ] `submission.yaml` exists with all required fields (see [openfe-benchmarks guide](https://github.com/OpenFreeEnergy/openfe-benchmarks#submitting-a-new-benchmark))
- [ ] `README.md` in submission directory describes the benchmark and any workflow deviations
- [ ] All scripts reference correct `openfe-benchmarks` locations and versions
- [ ] No hardcoded credentials or secrets in any files

### Directory Structure

- [ ] `create_network/` contains planning script and generated network
- [ ] `get_results/` contains metadata preparation script and output artifacts
- [ ] `alchemiscale_submission.ipynb` for Alchemiscale submission (if applicable)
- [ ] No temporary files, credentials, or `.DS_Store` files included

## Examples to Reference

- **RBFE example**: `submissions/2026_03_17_openff-2.3.0_jacs_tyk2/`
- **ASFE examples**: `submissions/2026_03_17_openff-2.3.0_freesolv/`, `submissions/2026_03_17_openff-2.3.0_mnsol/`

## Development notes

- Python: requires Python >= 3.11 (see `pyproject.toml`).
- This repository provides helpers; it does not provide operational support for running alchemiscale.

## License

This project is released under the MIT License — see `LICENSE`.
