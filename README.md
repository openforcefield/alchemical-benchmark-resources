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

Place each submission in `submissions/<directory-name>/`. The directory name should be descriptive (e.g., `2026_03_17_openff-2.3.0_freesolv`). The directory **must** contain a YAML metadata file named `submission.yaml`.

Required files and fields

- `submissions/<directory-name>/submission.yaml` (required)
  - Required YAML fields:
    - `submission_id`: string — unique, kebab-case identifier for this submission
    - `title`: string — short descriptive title
    - `summary`: string — short descriptive summary (1–2 sentences)
    - `tags`: list — relevant tags (e.g., `[asfe, openff-2.3.0, nagl_openff-gnn-am1bcc-1.0.0.pt, openfe, alchemicalarchive]`)
    - `authors`: list of dicts with `name` and optional `affiliation` and `ORCID`
    - `date`: string — publication/submission date (ISO 8601 format)
    - `openfe_version`: string — OpenFE version used
    - `openmm_version`: string — OpenMM version used (optional)
    - `openff_toolkit_version`: string — OpenFF toolkit version used
    - `forcefield`: string — force field used (e.g., `openff-2.3.0`)
    - `partial_charges`: string — partial charge model used
    - `network`: string — network identifier
    - `benchmark_data`: dict with `source_repository`, `set`, and `system` fields
    - `archive`: dict with `doi` and `archive_provider` fields (long-term archive pointer)
    - `license`: string — license for the submission (e.g., `CC-BY-4.0`)
  - Optional fields:
    - `protocol_settings`: dict or list of dicts with protocol-specific settings

- Supporting files (optional but recommended):
  - Python input script: include any custom `.py` file used to generate the submission
  - JSON or compressed network files: alchemical network definitions
  - README.md: document any workflow details that deviate from standard examples

Example minimal `submission.yaml`

```yaml
submission_id: 2026-02-01-example-recycle
title: Recycled network with openff-2.1.0 and AM1-BCC charges
summary: |
  This submission describes a recycled alchemical network prepared with openff-2.1.0
  and AM1-BCC partial charges. The archive contains X transformations.
tags: [recycled, openff-2.1.0, asfe, openfe]
authors:
  - name: My Name
    affiliation: My Institution
date: 2026-02-10
openfe_version: 1.8.0
openmm_version: 8.1.1
openff_toolkit_version: 0.16.0
forcefield: openff-2.1.0
partial_charges: AM1-BCC
network: example-network-id
benchmark_data:
  source_repository: https://github.com/OpenFreeEnergy/openfe-benchmarks
  set: solvation_set
  system: example-system
archive:
  doi: "10.5281/zenodo.example"
  archive_provider: zenodo
license: CC-BY-4.0
protocol_settings:
  - protocol: AbsoluteSolvationProtocol
    production_time: "10.0 nanosecond"
    equilibration_time: "0.5 nanosecond"
``` 

## Examples and recommended scripts

- Refer to `openfe-benchmarks` example scripts (for canonical workflow examples) by setting `script` to the example script path, e.g. `openfe-benchmarks/scripts/_example_rdfe.py`.

## Checklist before creating a pull request

1. Ensure `submissions/<directory-name>/submission.yaml` exists with all required fields.
2. Verify the `submission_id` is unique and follows kebab-case format.
3. Include all required software versions: `openfe_version`, `openmm_version`, `openff_toolkit_version`.
4. Provide complete `benchmark_data` provenance (source repository, set, system).
5. Populate `archive` with at least a DOI or archive provider URL.
6. Include any custom `.py` input script or planning script in the submission directory.
7. Add a short README or notes in the submission directory if the workflow deviates from the examples.
8. Use valid ISO 8601 date format (YYYY-MM-DD) in the `date` field.

## Development notes

- Python: requires Python >= 3.11 (see `pyproject.toml`).
- This repository provides helpers; it does not provide operational support for running alchemiscale.

## License

This project is released under the MIT License — see `LICENSE`.
