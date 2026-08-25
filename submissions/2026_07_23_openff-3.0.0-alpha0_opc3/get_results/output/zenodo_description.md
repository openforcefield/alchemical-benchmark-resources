# OpenFE RBFE - jacs_set (8 systems) - 2026_08_05_openff-3.0.0-alpha0_opc3_jacs

## Overview
RBFE benchmark results prepared from AlchemicalArchive JSON file(s) generated with OpenFE and Alchemiscale.

This submission describes the RBFE benchmark covering the jacs_set benchmark set (bace, cdk2, jnk1,
mcl1, p38, ptp1b, thrombin, tyk2) prepared with opc3.offxml/openff-3.0.0-alpha0 for proteins and
solvents, and openff-3.0.0-alpha0 with nagl_openff-gnn-am1bcc-1.0.0.pt for ligands, solutes, and
cofactors. The network contains 566 edges across 194 unique ligands. Results are derived from
archived Alchemiscale workflow data. For scripts to generate this network:
github.com/openforcefield/alchemical-benchmark-
resources/submissions/2026_07_23_openff-3.0.0-alpha0_opc3/alchemiscale_submission.ipynb

## Repository Reference
This submission is linked from the OpenFE Benchmarks repository:
https://github.com/OpenFreeEnergy/openfe-benchmarks/tree/main/openfe_benchmarks/results/2026_08_05_openff-3.0.0-alpha0_opc3_jacs

## Software Versions
openfe_version: "1.8.0"
openmm_version: "8.2.0"
openff_toolkit_version: "0.18"

## Alchemical Network Keys
  - AlchemicalNetwork-0482bbeceac4470dd4c29afeadfa5825: jacs_set/bace
  - AlchemicalNetwork-21aba16db838ca5833ad036c37ee50d2: jacs_set/mcl1
  - AlchemicalNetwork-7420dd6f7be012084483a3d57faa2350: jacs_set/jnk1
  - AlchemicalNetwork-c7614ad07bf6ffffd3369475e628e20e: jacs_set/ptp1b
  - AlchemicalNetwork-ea6d43b749172c8d7df19a66bec9838a: jacs_set/tyk2
  - AlchemicalNetwork-ea875d9e2896b0e337a17bf950c722ba: jacs_set/cdk2
  - AlchemicalNetwork-febece7a6c1eb4f964a57f994934a31a: jacs_set/thrombin
  - AlchemicalNetwork-ff43514f04705b71bcb834c34c8e51b0: jacs_set/p38

## Recommended Descriptors
forcefield: ["opc3.offxml", "openff-3.0.0-alpha0"]
small_molecule_forcefield: "openff-3.0.0-alpha0"
partial_charges: nagl_openff-gnn-am1bcc-1.0.0.pt
mapper: "KartografAtomMapper 1.2.0 (LSA)"


## BenchmarkData Provenance
  (from openfe-benchmarks planning script) with associated network key benchmark_data:
  source_repository: https://github.com/OpenFreeEnergy/openfe-benchmarks
  "jacs_set":
    "bace": AlchemicalNetwork-0482bbeceac4470dd4c29afeadfa5825
    "cdk2": AlchemicalNetwork-ea875d9e2896b0e337a17bf950c722ba
    "jnk1": AlchemicalNetwork-7420dd6f7be012084483a3d57faa2350
    "mcl1": AlchemicalNetwork-21aba16db838ca5833ad036c37ee50d2
    "p38": AlchemicalNetwork-ff43514f04705b71bcb834c34c8e51b0
    "ptp1b": AlchemicalNetwork-c7614ad07bf6ffffd3369475e628e20e
    "thrombin": AlchemicalNetwork-febece7a6c1eb4f964a57f994934a31a
    "tyk2": AlchemicalNetwork-ea6d43b749172c8d7df19a66bec9838a


## Protocol Settings
protocol_settings:
  - protocol: "HybridTopProtocol"
    protocol_library: "pontibus"
    timestep: "4.0 fs"
    temperature: "298.15 K"
    pressure: "1 bar"
    forcefields: ["opc3.offxml", "openff-3.0.0-alpha0"]
    small_molecule_forcefield: "openff-3.0.0-alpha0"
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
      - AlchemicalNetwork-0482bbeceac4470dd4c29afeadfa5825 jacs_set-bace: ligand_start=CAT-13a, ligand_final=CAT-13c, solvent={'O'}, cofactors=none, protein={'unknown'}
      - AlchemicalNetwork-0482bbeceac4470dd4c29afeadfa5825 jacs_set-bace: ligand_start=CAT-13a, ligand_final=CAT-13f, solvent={'O'}, cofactors=none, protein={'unknown'}
      - AlchemicalNetwork-0482bbeceac4470dd4c29afeadfa5825 jacs_set-bace: ligand_start=CAT-13a, ligand_final=CAT-13g, solvent={'O'}, cofactors=none, protein={'unknown'}
      - AlchemicalNetwork-0482bbeceac4470dd4c29afeadfa5825 jacs_set-bace: ligand_start=CAT-13a, ligand_final=CAT-13i, solvent={'O'}, cofactors=none, protein={'unknown'}
      - AlchemicalNetwork-0482bbeceac4470dd4c29afeadfa5825 jacs_set-bace: ligand_start=CAT-13a, ligand_final=CAT-13o, solvent={'O'}, cofactors=none, protein={'unknown'}
      - etc.
  - protocol: "HybridTopProtocol"
    notes: |
      Detailed protocol settings differ:
      - solvation_settings.solvent_padding: 1 -> 1.2
      Applies to 283 edges:
      - AlchemicalNetwork-0482bbeceac4470dd4c29afeadfa5825 jacs_set-bace: ligand_start=CAT-13a, ligand_final=CAT-13c, solvent={'O'}, cofactors=none, protein=none
      - AlchemicalNetwork-0482bbeceac4470dd4c29afeadfa5825 jacs_set-bace: ligand_start=CAT-13a, ligand_final=CAT-13f, solvent={'O'}, cofactors=none, protein=none
      - AlchemicalNetwork-0482bbeceac4470dd4c29afeadfa5825 jacs_set-bace: ligand_start=CAT-13a, ligand_final=CAT-13g, solvent={'O'}, cofactors=none, protein=none
      - AlchemicalNetwork-0482bbeceac4470dd4c29afeadfa5825 jacs_set-bace: ligand_start=CAT-13a, ligand_final=CAT-13i, solvent={'O'}, cofactors=none, protein=none
      - AlchemicalNetwork-0482bbeceac4470dd4c29afeadfa5825 jacs_set-bace: ligand_start=CAT-13a, ligand_final=CAT-13o, solvent={'O'}, cofactors=none, protein=none
      - etc.


## Rights
- License: CC-BY-4.0
