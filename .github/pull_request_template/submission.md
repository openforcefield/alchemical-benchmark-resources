## New Alchemical Benchmark Submission

This PR adds a new alchemical benchmark submission to the repository.

---

## Pre-Submission Checklist

### Network Creation & Validation

- [ ] Network generation script is included in `submissions/<directory>/create_network/`
- [ ] Network JSON file exists and is valid JSON
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

---

## Submission Details

**Benchmark Set:** <!-- e.g., JACS TYK2, FreeSolv, etc. -->

**Transformation Type:** <!-- RBFE or ASFE -->

**Force Field:** <!-- e.g., OpenFF 2.3.0 -->

**Water Model:** <!-- e.g., OPC3, TIP3P -->

**Deviations from Standard Workflow:** <!-- Any non-standard steps or parameters used -->

---

## Additional Notes

<!-- Add any additional context or special instructions here -->
