# Alchemical Benchmark Submission Workflow

This guide walks through the complete process of preparing and submitting an alchemical benchmark to the OpenFE benchmarks repository. It uses the `2026_03_17_openff-2.3.0_jacs_tyk2` submission as a working example throughout.

## Overview

A complete submission workflow has three main phases:

1. **Network Creation Phase** — Design and generate the alchemical network
2. **Computation Phase** — Run calculations on Alchemiscale infrastructure
3. **Results & Metadata Phase** — Gather results and prepare submission artifacts

## Phase 1: Network Creation

### 1.1 Acquire or Create the Alchemical Network

Start with a planning script that generates your alchemical network. The network defines all the molecular transformations you want to calculate.

**Example**: The `jacs-tyk2` submission uses `plan_tyk2_rbfe.py` in the `create_network/` directory, adapted from `openfe_benchmarks/_example_plan_rbfe.py`. Always use up to date scripts form `openfe_benchmarks`

**Key decisions when creating your plan script:**

- **Benchmark system**: Which benchmark set and system? (e.g., `jacs_set/tyk2`)
- **Force field**: Which OpenFF force field version? (e.g., `openff-2.3.0`)
- **Partial charges**: Which charge model? (e.g., `nagl_openff-gnn-am1bcc-1.0.0.pt`)
- **Protocol repeats**: How many replicate runs? (Start with 1 for testing)
- **Solvent**: Which solvent model? (Most commonly neutral with salt, e.g., `SolventComponent(neutralize=True)`)

**Example snippet from `plan_tyk2_rbfe.py`:**

```python
SOLVENT = SolventComponent(neutralize=True)
BENCHMARK_SET = "jacs_set"
BENCHMARK_SYS = "tyk2"
PARTIAL_CHARGE = "nagl_openff-gnn-am1bcc-1.0.0.pt"
FORCEFIELD = "openff-2.3.0"
```

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
│   └── alchemical_network_jacs_set_tyk2.json  # Generated network
```

## Phase 2: Computation Phase

### 2.1 Set Up Alchemiscale Credentials

Before running on Alchemiscale, configure your credentials as described in the [Alchemiscale User Guide](https://docs.alchemiscale.org/en/stable/user_guide/getting_started.html#instantiating-an-alchemiscaleclient).

Save credentials to your system (typically `~/.config/alchemiscale/` or environment variables `ALCHEMISCALE_ID` and `ALCHEMISCALE_KEY`).

### 2.2 Define Scope

An Alchemiscale Scope is defined as `Scope(org, campaign, project)` and tracks your computation within Alchemiscale's infrastructure.

**Example Scope**: `Scope('openff', 'openff_2_3_0', 'jacs_tyk2')`

Where:
- **org** = Organization name (e.g., `'openff'`)
- **campaign** = Campaign name, typically the forcefield version (e.g., `'openff_2_3_0'`)
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

**Example workflow in notebook:**

```python
from alchemiscale import AlchemiscaleClient, Scope
import openfe

# Connect to Alchemiscale
asc = AlchemiscaleClient("https://api.alchemiscale.org", 
                         user_id=user_id, 
                         user_key=user_key)

# Load network
network = openfe.AlchemicalNetwork.from_json("alchemical_network_jacs_set_tyk2.json")

# Define scope
scope = Scope("openff", "openff_2_3_0_v2", "jacs_tyk2")

# Submit
network_key = asc.push_network(network, scope)

# Monitor (typically via web dashboard)
```

After submission, monitor job completion through Alchemiscale's web interface or programmatically.

## Phase 3: Results & Metadata Phase

### 3.1 Gather Alchemical Archive

Once all computations complete, retrieve the full network archive using the gather script:

```bash
python get_results/_no_test_example_prepare_metadata.py
```

This script:
1. Retrieves the network from Alchemiscale using the network key
2. Generates `computational_results.json` with all calculation results
3. Prepares submission metadata

**Expected output files in `get_results/output/`:**

- `AlchemicalNetwork-<gufe-hash>-openff-<campaign>-<project>.json.bz2` — Compressed network archive
- `computational_results.json` — Extracted computational results
- `submission.yaml` — Submission metadata

### 3.2 Prepare Submission Metadata

The metadata preparation script generates `submission.yaml` with all required submission fields. For complete documentation on metadata fields, requirements, and examples, see the [OpenFE Benchmarks Submission Guide](https://github.com/OpenFreeEnergy/openfe-benchmarks#submitting-a-new-benchmark).

### 3.3 Generate Zenodo Description (Optional but Recommended)

The metadata script also generates `zenodo_description.md` for use when archiving to Zenodo:

- Summarizes the network and calculation settings
- Documents the computation metadata
- Useful for long-term archival and citations

### 3.4 Organize Final Submission

Your final submission directory should look like:

```
submissions/2026_03_17_openff-2.3.0_jacs_tyk2/
├── README.md                           # Overview and workflow notes
├── submission.yaml                      # Submission metadata (required)
├── create_network/
│   ├── plan_tyk2_rbfe.py               # Planning script used
│   └── alchemical_network_jacs_set_tyk2.json  # Generated network
├── get_results/
│   ├── _no_test_example_prepare_metadata.py  # Metadata preparation script
│   ├── log.txt                         # Execution log
│   └── output/
│       ├── AlchemicalNetwork-<hash>.json.bz2  # Network archive
│       ├── computational_results.json   # Extracted results
│       └── zenodo_description.md       # (Optional) Archive description
├── alchemiscale_submission.ipynb       # Notebook for compute submission
└── alchemicalnetwork_scopekeys.txt     # Record of Scope keys used
```

## Pre-Submission Checklist

Before creating a pull request to `openfe-benchmarks`:

### Metadata & Documentation

- [ ] `submission.yaml` exists in submission directory
- [ ] For complete metadata field requirements, see [openfe-benchmarks submission documentation](https://github.com/OpenFreeEnergy/openfe-benchmarks#submission-metadata)
- [ ] `README.md` in submission directory documents any workflow deviations

### Files & Structure

- [ ] `create_network/` contains:
  - [ ] Planning script that generated the network
  - [ ] Generated alchemical network JSON file
- [ ] `get_results/` contains:
  - [ ] Metadata preparation script with clear network key and parameters
  - [ ] `output/` subdirectory with:
    - [ ] Compressed network archive (`.json.bz2`)
    - [ ] `computational_results.json` with actual results
- [ ] All scripts are reproducible and reference `openfe-benchmarks` utilities where applicable

### Workflow & Reproducibility

- [ ] Verify network generation runs without errors
- [ ] Confirm all transformations in network are valid
- [ ] Document any custom parameters or modifications in README.md
- [ ] Ensure scope keys are recorded in `alchemicalnetwork_scopekeys.txt`
- [ ] Verify Zenodo archive metadata is complete (if archiving externally)

### Code Quality

- [ ] No temporary or debug files included
- [ ] All script file paths reference correct locations in openfe-benchmarks
- [ ] No hardcoded paths or credentials in scripts

## Common Variations & Examples

### Solvation Free Energy (ASFE) vs Relative Binding Free Energy (RBFE)

This guide focuses on RBFE (as in the `jacs_tyk2` example), but ASFE submissions follow similar structure:

- Use `plan_asfe_*.py` scripts instead of `plan_rbfe_*.py`
- Set `network: solvation_set/<system_name>`
- Protocol will be `AbsoluteSolvationProtocol` instead of `RelativeHybridTopologyProtocol`

### Multiple Force Fields or Charge Models

If you're submitting multiple variants:

Create separate submission directories for each:

```
submissions/2026_07_15_openff-3.0.0-alpha1b_opc3/
submissions/2026_07_15_openff-3.0.0-alpha1b_tip3p/
```

## Troubleshooting

### Network Fails Validation

**Problem**: The planning script throws validation errors when generating the network.

**Solutions**:
- Check that all molecules in the benchmark system are valid
- Verify the force field and charge model combination is supported
- Review protein preparation (is PDB valid?)
- Check for missing cofactors or special handling needed

### Alchemiscale Connection Issues

**Problem**: Cannot connect to Alchemiscale API.

**Solutions**:
- Verify credentials are correctly configured in environment or config file
- Check network connectivity to `https://api.alchemiscale.org`
- Consult [Alchemiscale User Guide](https://docs.alchemiscale.org/en/stable/user_guide/index.html)

### Results Gathering Fails

**Problem**: `_no_test_example_prepare_metadata.py` cannot find network or results.

**Solutions**:
- Verify the `NETWORK_KEY` in the script matches the key from Alchemiscale submission
- Confirm all jobs in Alchemiscale have completed successfully
- Check network connectivity and credentials

### Missing or Incomplete Results

**Problem**: `computational_results.json` is missing entries or truncated.

**Solutions**:
- Verify all transformation calculations completed in Alchemiscale
- Re-run the gather script or check logs for errors
- May indicate partial failure — review Alchemiscale job logs

## References

- [OpenFE Documentation](https://docs.openfree.energy/)
- [Alchemiscale User Guide](https://docs.alchemiscale.org/en/stable/user_guide/index.html)
- [OpenFE Benchmarks Repository](https://github.com/OpenFreeEnergy/openfe-benchmarks)
- [OpenFF Toolkit Documentation](https://open-forcefield-toolkit.readthedocs.io/)

## Support

For detailed questions about specific components:

- **Network design**: See `openfe-benchmarks/scripts/` for examples
- **Alchemiscale infrastructure**: Consult [Alchemiscale documentation](https://docs.alchemiscale.org/)
- **OpenFE protocols**: Refer to [OpenFE tutorials](https://docs.openfree.energy/en/latest/tutorials/)
