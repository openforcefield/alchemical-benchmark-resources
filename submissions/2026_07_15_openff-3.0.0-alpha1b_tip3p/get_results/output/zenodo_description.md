# OpenFE RBFE - jacs_set (8 systems) - 2026-08-05-openff3.0.0-alpha1b_tip3p-jacs

## Overview
RBFE benchmark results prepared from AlchemicalArchive JSON file(s) generated with OpenFE and Alchemiscale.

This submission describes the RBFE benchmark covering the jacs_set benchmark set (bace, cdk2, jnk1,
mcl1, p38, ptp1b, thrombin, tyk2) prepared with openff-3.0.0-alpha1b/tip3p.offxml for proteins and
solvents, and openff-3.0.0-alpha1b with nagl_openff-gnn-am1bcc-1.0.0.pt for ligands, solutes, and
cofactors. The network contains 566 edges across 194 unique ligands. Results are derived from
archived Alchemiscale workflow data. For scripts to generate this network:
github.com/openforcefield/alchemical-benchmark-
resources/submissions/2026_07_15_openff-3.0.0-alpha1b_tip3p/alchemiscale_submission.ipynb

## Repository Reference
This submission is linked from the OpenFE Benchmarks repository:
https://github.com/OpenFreeEnergy/openfe-benchmarks/tree/main/openfe_benchmarks/results/2026-08-05-openff3.0.0-alpha1b_tip3p-jacs

## Software Versions
openfe_version: "1.8.0"
openmm_version: "8.2.0"
openff_toolkit_version: "0.18"

## Alchemical Network Keys
  - AlchemicalNetwork-28ff87e9e98dcc018873a3d0f364c0cd: jacs_set/cdk2
  - AlchemicalNetwork-38e7552634bee5f4d425fe9ed2fb85d9: jacs_set/bace
  - AlchemicalNetwork-5a1747bd8d2fec35462d32168df71c4f: jacs_set/ptp1b
  - AlchemicalNetwork-5aca98623a3487f76f1fd7255848a4a9: jacs_set/mcl1
  - AlchemicalNetwork-7337defddce50b480590f8c848143d65: jacs_set/p38
  - AlchemicalNetwork-79b5a746219163f999ed27182064a7d0: jacs_set/jnk1
  - AlchemicalNetwork-8f28971733a4f639c9ba89cba74466f9: jacs_set/thrombin
  - AlchemicalNetwork-f8388a2e4aa7e6909e505ae1e61b4e12: jacs_set/tyk2

## Recommended Descriptors
forcefield: ["openff-3.0.0-alpha1b", "tip3p.offxml"]
small_molecule_forcefield: "openff-3.0.0-alpha1b"
partial_charges: nagl_openff-gnn-am1bcc-1.0.0.pt
mapper: "KartografAtomMapper 1.2.0 (LSA)"


## BenchmarkData Provenance
  (from openfe-benchmarks planning script) with associated network key benchmark_data:
  source_repository: https://github.com/OpenFreeEnergy/openfe-benchmarks
  "jacs_set":
    "bace": AlchemicalNetwork-38e7552634bee5f4d425fe9ed2fb85d9
    "cdk2": AlchemicalNetwork-28ff87e9e98dcc018873a3d0f364c0cd
    "jnk1": AlchemicalNetwork-79b5a746219163f999ed27182064a7d0
    "mcl1": AlchemicalNetwork-5aca98623a3487f76f1fd7255848a4a9
    "p38": AlchemicalNetwork-7337defddce50b480590f8c848143d65
    "ptp1b": AlchemicalNetwork-5a1747bd8d2fec35462d32168df71c4f
    "thrombin": AlchemicalNetwork-8f28971733a4f639c9ba89cba74466f9
    "tyk2": AlchemicalNetwork-f8388a2e4aa7e6909e505ae1e61b4e12


## Protocol Settings
protocol_settings:
  - protocol: "HybridTopProtocol"
    protocol_library: "pontibus"
    timestep: "4.0 fs"
    temperature: "298.15 K"
    pressure: "1 bar"
    forcefields: ["openff-3.0.0-alpha1b", "tip3p.offxml"]
    small_molecule_forcefield: "openff-3.0.0-alpha1b"
    partial_charges: "nagl_openff-gnn-am1bcc-1.0.0.pt"
    equilibration_time: "1.0 ns"
    production_time: "5.0 ns"
    vacuum_equilibration_time: 
    vacuum_production_time: 
    solvent_equilibration_time: 
    solvent_production_time: 
    lambda_functions: "default"
    lambda_windows: "11"
    lambda_schedule: ""
    notes: |
      Applies to 283 edges:
      - AlchemicalNetwork-28ff87e9e98dcc018873a3d0f364c0cd jacs_set-cdk2: ligand_start=17, ligand_final=1h1q, solvent={'O'}, cofactors=none, protein={'unknown'}
      - AlchemicalNetwork-28ff87e9e98dcc018873a3d0f364c0cd jacs_set-cdk2: ligand_start=17, ligand_final=1h1r, solvent={'O'}, cofactors=none, protein={'unknown'}
      - AlchemicalNetwork-28ff87e9e98dcc018873a3d0f364c0cd jacs_set-cdk2: ligand_start=17, ligand_final=1oiu, solvent={'O'}, cofactors=none, protein={'unknown'}
      - AlchemicalNetwork-28ff87e9e98dcc018873a3d0f364c0cd jacs_set-cdk2: ligand_start=1h1r, ligand_final=1h1q, solvent={'O'}, cofactors=none, protein={'unknown'}
      - AlchemicalNetwork-28ff87e9e98dcc018873a3d0f364c0cd jacs_set-cdk2: ligand_start=1h1s, ligand_final=31, solvent={'O'}, cofactors=none, protein={'unknown'}
      - etc.
  - protocol: "HybridTopProtocol"
    notes: |
      Detailed protocol settings differ:
      - solvation_settings.solvent_padding: 1 -> 1.2
      Applies to 283 edges:
      - AlchemicalNetwork-28ff87e9e98dcc018873a3d0f364c0cd jacs_set-cdk2: ligand_start=17, ligand_final=1h1q, solvent={'O'}, cofactors=none, protein=none
      - AlchemicalNetwork-28ff87e9e98dcc018873a3d0f364c0cd jacs_set-cdk2: ligand_start=17, ligand_final=1h1r, solvent={'O'}, cofactors=none, protein=none
      - AlchemicalNetwork-28ff87e9e98dcc018873a3d0f364c0cd jacs_set-cdk2: ligand_start=17, ligand_final=1oiu, solvent={'O'}, cofactors=none, protein=none
      - AlchemicalNetwork-28ff87e9e98dcc018873a3d0f364c0cd jacs_set-cdk2: ligand_start=1h1r, ligand_final=1h1q, solvent={'O'}, cofactors=none, protein=none
      - AlchemicalNetwork-28ff87e9e98dcc018873a3d0f364c0cd jacs_set-cdk2: ligand_start=1h1s, ligand_final=31, solvent={'O'}, cofactors=none, protein=none
      - etc.


## Rights
- License: CC-BY-4.0
