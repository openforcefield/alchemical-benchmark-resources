# Alchemical Benchmark Submission Workflow

This guide walks through the complete process of preparing and submitting an alchemical benchmark to the OpenFE benchmarks repository. It uses the `2026_03_17_openff-2.3.0_jacs_tyk2` submission as a working example throughout.

## Overview

A complete submission workflow has three main phases:

1. **Network Creation Phase** — Design and generate the alchemical network - merge PR for review
2. **Computation Phase** — Run calculations on Alchemiscale infrastructure
3. **Results & Metadata Phase** — Gather results and prepare submission artifacts - merge PR without review

## Phase 1: Network Creation

### 1.1 Acquire or Create the Alchemical Network

Start with a planning script that generates your alchemical network. The network defines all the molecular transformations you want to calculate.

**Example**: The `jacs-tyk2` submission uses `plan_tyk2_rbfe.py` in the `create_network/` directory, adapted from `openfe_benchmarks/_example_plan_rbfe.py`. Always use up to date scripts form `openfe_benchmarks`

**Key decisions when creating your plan script:**

- **Benchmark system**: Which benchmark set and system(s)? (e.g., `jacs_set/tyk2`)
- **Force field**: Which OpenFF force field version? (e.g., `openff-2.3.0`)
- **Partial charges**: Which charge model? See openfe-benchmarks for defined options, e.g., `nagl_openff-gnn-am1bcc-1.0.0.pt`
- **Solvent**: Which solvent model? (Most commonly neutral with salt, e.g., `SolventComponent(neutralize=True)`)
- **Protocol repeats**: How many replicate runs? Commonly, 1 is used and replicates are handled on alchemiscale. If running on an HPC, consider 3


### 1.2 Generate and Validate the Network

Run your planning script to generate the alchemical network JSON file.

```bash
python create_network/plan_tyk2_rbfe.py
```

**Expected output**: A JSON file (e.g., `alchemical_network_jacs_set_tyk2.json`) containing all transformation definitions.

**Validation checks:**

- Does the network JSON file exist and contain valid transformation objects?
- Are all molecular components properly parameterized?
- Does the file size seem reasonable for your system count? (Check for obvious encoding errors)

### 1.3 Organize Network Files

Place the generated network and planning script in a `create_network/` subdirectory of your submission:

```
submissions/2026_03_17_openff-2.3.0_jacs_tyk2/
├── create_network/
│   ├── plan_tyk2_rbfe.py           # Original planning script
|   |   log.txt
│   └── alchemical_network_jacs_set_tyk2.json  # Generated network (gitignored)
```

### 1.4 Submit a PR for Review

Commit the `plan_tyk2_rbfe.py` and associated `log.txt` files and create a PR for review by the science team. These are expensive calculations and we want to ensure that our target experiments are successful.

## Phase 2: Computation Phase

### 2.1 Set Up Alchemiscale Credentials

Before running on Alchemiscale, configure your credentials as described in the [Alchemiscale User Guide](https://docs.alchemiscale.org/en/stable/user_guide/getting_started.html#instantiating-an-alchemiscaleclient).

### 2.2 Define Scope

An Alchemiscale Scope is defined as `Scope(org, campaign, project)` and tracks your computation within Alchemiscale's infrastructure.

**Example Scope**: `Scope('openff', 'openff_2_3_0', 'jacs_tyk2')`

Where:
- **org** = Organization name (e.g., `'openff'`)
- **campaign** = Campaign name, maybe the forcefield version (e.g., `'openff_2_3_0'`)
- **project** = Specific network identifier (e.g., `'jacs_tyk2'`)

When you submit the same scope multiple times, Alchemiscale tracks different runs with unique identifiers (gufe tokens).

**Example Scope keys observed in practice:**

```
ScopedKey('AlchemicalNetwork-ba0d4a6110f9c5dffd20d5f56503a7f4-openff-openff_2_3_0-freesolv')
ScopedKey('AlchemicalNetwork-518a69101fba8b29bbb6fbb6b0ba9a5d-openff-openff_2_3_0_rc1-mnsol')
```

### 2.3 Submit and Run on Alchemiscale

Use an interactive notebook (e.g., `alchemiscale_submission.ipynb`) to:

1. Load your alchemical network JSON
2. Connect to Alchemiscale with your credentials
3. Define your Scope
4. Submit the network and transformations
5. Monitor execution

After submission, monitor job completion through Alchemiscale's web interface or programmatically (See other notebooks in this repository).

### 2.4 Add a Restart Pattern

Consider adding a restart pattern so that if an error occurs for a known hardware reason, the calculation is automatically resubmit.

## Phase 3: Results & Metadata Phase

### 3.1 Gather Alchemical Archive

Once all computations complete, retrieve the full network archive using gather scripts like `_no_test_example_rbfe_submission.py` (always get a current version from the repository).

This script:
1. Retrieves the network from Alchemiscale using the network key
2. Generates `computational_results.json` with all calculation results
3. Prepares submission metadata

**Expected output files in `get_results/output/`:**

- `AlchemicalNetwork-<gufe-hash>-openff-<campaign>-<project>.json.bz2` — Compressed network archive
- `computational_results.json` — Extracted computational results
- `submission.yaml` — Submission metadata

### 3.2 Prepare Submission Metadata

The metadata preparation script generates `submission.yaml` with all required submission fields, except those marked with `TODO`. For complete documentation on metadata fields, requirements, and examples, see the [OpenFE Benchmarks Repository](https://github.com/OpenFreeEnergy/openfe-benchmarks).

### 3.3 Generate Zenodo Description (Optional but Recommended)

The metadata script also generates `zenodo_description.md` for use when archiving to Zenodo:

- Summarizes the network and calculation settings, note the `summary_suffix` field to add additional details such as a reference to this repository.
- Documents the computation metadata
- Useful for long-term archival and citations
- Contains `TODO` items before copy/paste

### 3.4 Organize Final Submission

Your final submission directory should look like:

```
submissions/2026_03_17_openff-2.3.0_jacs_tyk2/
├── README.md                           # (required) Overview and workflow notes
├── create_network/
│   ├── plan_tyk2_rbfe.py               # (required) Planning script used
│   ├── log.txt                         # (required) Log file from running planning script
│   └── alchemical_network_jacs_set_tyk2.json  # (do not commit) Generated network
├── get_results/
│   ├── _no_test_example_prepare_metadata.py  # (required) Metadata preparation script
│   ├── log.txt                         # (required) Execution log
│   └── output/
│       ├── AlchemicalNetwork-<hash>.json.bz2  # (do not commit) Network archive
│       ├── computational_results.json   # (required) Extracted results
│       ├── submission.yaml             # (required) Submission metadata
│       └── zenodo_description.md       # (required) Archive description
├── alchemiscale_submission.ipynb       # (required) Notebook for compute submission
└── alchemicalnetwork_scopekeys.txt     # (required) Record of Scope keys used
```

### Multiple Force Fields or Charge Models

If you're submitting multiple variants:

Create separate submission directories for each:

```
submissions/2026_07_15_openff-3.0.0-alpha1b_opc3/
submissions/2026_07_15_openff-3.0.0-alpha1b_tip3p/
```

## Support

For detailed questions about specific components:

- **Network design**: See `openfe-benchmarks/scripts/` for examples
- **Alchemiscale infrastructure**: Consult [Alchemiscale documentation](https://docs.alchemiscale.org/)
- **OpenFE protocols**: Refer to [OpenFE tutorials](https://docs.openfree.energy/en/latest/tutorials/)
