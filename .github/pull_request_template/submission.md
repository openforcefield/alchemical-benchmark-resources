## Alchemical Benchmark Submission

This PR submits a new alchemical benchmark. **Please select your submission type below.**

---

## Submission Type

- [ ] **Pre-Calculation** — Network creation phase (Phase 1). Requires science team review before computation begins.
- [ ] **Post-Calculation** — Results and metadata phase (Phase 3). Corresponds to a merged PR in [openfe-benchmarks](https://github.com/OpenFreeEnergy/openfe-benchmarks).

---

## PRE-CALCULATION SUBMISSION CHECKLIST

*Use this checklist if you selected **Pre-Calculation** above. This phase requires review before running calculations on Alchemiscale.*

### Network Creation & Validation

- [ ] Network generation script is included in `submissions/<directory>/create_network/plan_*.py`
- [ ] Log file from running the script exists: `submissions/<directory>/create_network/log.txt`
- [ ] Network JSON file was generated and validates correctly as shown in the log file (do not commit the JSON file itself)
- [ ] Script runs without errors: `python create_network/plan_*.py`
- [ ] All molecular components are properly parameterized
- [ ] Network file size is reasonable for the transformation count (**RBFE**: ~1–2 MB per 100 transforms; **ASFE**: ~0.7 MB per 1000 transforms)
- [ ] Script uses up-to-date utilities from current `openfe-benchmarks` version

### Planning Documentation

- [ ] `README.md` in submission directory describes the benchmark, system, and methodology
- [ ] Key decisions documented: benchmark set, force field, charge model, solvent, protocol repeats
- [ ] Any deviations from standard workflow are clearly noted
- [ ] No hardcoded credentials or secrets in any files

### Directory Structure (Phase 1 Only)

- [ ] `submissions/<directory>/create_network/` contains:
  - `plan_*.py` (planning script)
  - `log.txt` (execution log)
- [ ] No generated network JSON, archives, or results files committed
- [ ] No `.DS_Store`, temporary files, or IDE artifacts included

---

## POST-CALCULATION SUBMISSION CHECKLIST

*Use this checklist if you selected **Post-Calculation** above. This phase corresponds to a merged PR in openfe-benchmarks and does not require additional scientific review.*

### Linked PR in openfe-benchmarks

- [ ] PR corresponding to this submission has been **merged** in [openfe-benchmarks](https://github.com/OpenFreeEnergy/openfe-benchmarks)
- [ ] Link to merged PR: <!-- Paste PR URL here -->

### Results Collection

- [ ] Alchemiscale submission completed successfully (all jobs finished)
- [ ] Network archive retrieved: `AlchemicalNetwork-<gufe-hash>.json.bz2` (do not commit)
- [ ] Computational results generated: `computational_results.json` with complete data
- [ ] Scope key(s) documented: `alchemicalnetwork_scopekeys.txt`
- [ ] Log file preserved: `get_results/log.txt`

### Metadata & Artifacts

- [ ] `submission.yaml` exists with all required fields (see [openfe-benchmarks](https://github.com/OpenFreeEnergy/openfe-benchmarks))
- [ ] `README.md` updated with results summary and any deviations from planned workflow
- [ ] All scripts use current versions from `openfe-benchmarks`
- [ ] No hardcoded credentials or secrets in any files
- [ ] `zenodo_description.md` generated for archival (optional but recommended)

### Directory Structure (Phase 3 Only)

- [ ] `submissions/<directory>/` contains:
  - `create_network/plan_*.py` and `create_network/log.txt` (from Phase 1)
  - `get_results/` with metadata script and `output/` subdirectory with `submission.yaml`, `zenodo_description.md` and `computational_results.json.bz2`
  - `alchemiscale_submission.ipynb` (notebook used for computation)
  - `alchemicalnetwork_scopekeys.txt`
  - `README.md`
- [ ] No temporary files, raw archives, or `.DS_Store` files included

---

## Submission Details (Both Types)

**Benchmark Set:** <!-- e.g., JACS TYK2, FreeSolv, mNSol, etc. -->

**Transformation Type:** <!-- RBFE or ASFE -->

**Force Field:** <!-- e.g., OpenFF 2.3.0, OpenFF 3.0.0-alpha1b -->

**Charge Model:** <!-- e.g., nagl_openff-gnn-am1bcc-1.0.0.pt -->

**Water Model:** <!-- e.g., OPC3, TIP3P, SPC, etc. -->

**Protocol Repeats:** <!-- How many replicate runs per transformation -->

---

## Additional Notes

<!-- Add any additional context, deviations from standard workflow, or special instructions here -->
