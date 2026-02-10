# alchemical-benchmark-resources

This repository provides utilities, example scripts and resources for preparing alchemical benchmark submissions to the OpenFE "openfe-benchmarks" repository for training and posterity within OpenFF.

## Purpose

- Provide reproducible tooling and examples for creating or recycling alchemical networks.
- Store submission-ready directories that match the naming and metadata conventions used by openfe-benchmarks.
- Offer example scripts (e.g. `recycle_network.py`) that can be used as input for generating networks and submission artifacts.
- Manage alchemiscale compute (separate from OpenFE)

## Submissions directory — required layout and metadata

Place each submission in `submissions/<submission-id>/`. The directory name **must** match the submission identifier used in the corresponding openfe-benchmarks entry and contain a YAML metadata file named `submission.yml`.

Required files and fields

- `submissions/<submission-id>/submission.yml` (required)
  - Required YAML fields (minimal):
    - `id`: string — submission identifier (must match directory name)
    - `title`: string
    - `authors`: list
    - `script`: path to the Python input script used for generating the submission (relative to the repository root)
    - `original_results`: path/URL/DOI to the source calculation being reused (if applicable)
    - `changes`: dict — brief description of changes (e.g. `{force_field: "openff-2.1.0", partial_charges: "AM1-BCC"}`)
    - `license`: license string
  - Optional but recommended fields: `date`, `notes`, `references`

- Python input script: either reference an existing example (for standard workflows) or include a unique script in the submission directory. If the submission uses a custom script, include that `.py` file in the same directory and set `script` in `submission.yml` to its relative path.

Example minimal `submission.yml`

```yaml
id: example-recycle-2026-02
title: Recycled network with ff and AM1-BCC charges
authors:
  - My Name
script: submissions/2026-02-example-recycle/recycle_network.py
original_results: path/to/original/results.tar.gz
changes:
  force_field: openff-2.1.0
  partial_charges: AM1-BCC
license: MIT
date: 2026-02-10
``` 

## Examples and recommended scripts

- Use `recycle_network.py` (present in this repository) for importing previous calculations and producing a cleaned network for submission.
- Refer to `openfe-benchmarks` example scripts (for canonical workflow examples) by setting `script` to the example script path, e.g. `openfe-benchmarks/scripts/_example_rdfe.py`.

## Checklist before creating a pull request

1. Ensure `submissions/<submission-id>/submission.yml` exists and `id` matches the directory name.
2. Include any custom `.py` input script in the submission directory and reference it in `submission.yml`.
3. Document provenance in `original_results` and list exactly what was changed in `changes`.
4. Add a short README or notes in the submission directory if the workflow deviates from the examples.

## Development notes

- Python: requires Python >= 3.11 (see `pyproject.toml`).
- This repository provides helpers; it does not provide operational support for running alchemiscale.

## License

This project is released under the MIT License — see `LICENSE`.
