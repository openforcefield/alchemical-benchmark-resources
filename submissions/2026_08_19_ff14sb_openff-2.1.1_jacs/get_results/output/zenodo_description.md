# OpenFE RBFE - jacs_set (8 systems) - 2026_08_25_ff14sb_openff-2.1.1_jacs

## Overview
RBFE benchmark results prepared from AlchemicalArchive JSON file(s) generated with OpenFE and Alchemiscale.

This submission describes the RBFE benchmark covering the jacs_set benchmark set (bace, cdk2, jnk1,
mcl1, p38, ptp1b, thrombin, tyk2) prepared with
ff14SB/lipid17_merged/phosaa10/tip3p_HFE_multivalent/tip3p_standard for proteins and solvents, and
openff-2.1.1 with am1bccelf10_oe for ligands, solutes, and cofactors. The network contains 566 edges
across 194 unique ligands. Results are derived from archived Alchemiscale workflow data. For scripts
to generate this network: github.com/openforcefield/alchemical-benchmark-
resources/submissions/2026_08_19_ff14sb_openff-2.1.1_jacs/alchemiscale_submission.ipynb

## Repository Reference
This submission is linked from the OpenFE Benchmarks repository:
https://github.com/OpenFreeEnergy/openfe-benchmarks/tree/main/openfe_benchmarks/results/2026_08_25_ff14sb_openff-2.1.1_jacs

## Software Versions
openfe_version: "1.8.0"
openmm_version: "8.2.0"
openff_toolkit_version: "0.18"

## Alchemical Network Keys
  - AlchemicalNetwork-47b82fc985880c624d46e880a904b41a: jacs_set/bace
  - AlchemicalNetwork-50b46f132fc0aef754007207960fb160: jacs_set/ptp1b
  - AlchemicalNetwork-88dbd6f8077f13dda9dd0161cbae6c27: jacs_set/tyk2
  - AlchemicalNetwork-9efd2cdc2013758827f60221d2f7e026: jacs_set/thrombin
  - AlchemicalNetwork-a77509bb2c2af02f4d2ff562d84904da: jacs_set/cdk2
  - AlchemicalNetwork-c24976d53044e75c6250c575efd12cd5: jacs_set/p38
  - AlchemicalNetwork-c35b0418d0b0187aa3e4ff756cc6a09a: jacs_set/mcl1
  - AlchemicalNetwork-f61c9321399bd7e0e7ce30320ce5cd6f: jacs_set/jnk1

## Recommended Descriptors
partial_charges: AM1BCC Elf10
mapper: "KartografAtomMapper 1.2.0 (LSA)"
forcefield: ["ff14SB", "lipid17_merged", "phosaa10", "tip3p_HFE_multivalent", "tip3p_standard"]
small_molecule_forcefield: "openff-2.1.1"


## BenchmarkData Provenance (from openfe-benchmarks planning script) with associated network key 
benchmark_data:
  source_repository: https://github.com/OpenFreeEnergy/openfe-benchmarks
  "jacs_set":
    "bace": AlchemicalNetwork-47b82fc985880c624d46e880a904b41a
    "cdk2": AlchemicalNetwork-a77509bb2c2af02f4d2ff562d84904da
    "jnk1": AlchemicalNetwork-f61c9321399bd7e0e7ce30320ce5cd6f
    "mcl1": AlchemicalNetwork-c35b0418d0b0187aa3e4ff756cc6a09a
    "p38": AlchemicalNetwork-c24976d53044e75c6250c575efd12cd5
    "ptp1b": AlchemicalNetwork-50b46f132fc0aef754007207960fb160
    "thrombin": AlchemicalNetwork-9efd2cdc2013758827f60221d2f7e026
    "tyk2": AlchemicalNetwork-88dbd6f8077f13dda9dd0161cbae6c27


## Protocol Settings
protocol_settings:
  - protocol: "RelativeHybridTopologyProtocol"
    protocol_library: "openfe"
    timestep: "4.0 fs"
    temperature: "298.15 K"
    pressure: "1 bar"
    forcefields: ["ff14SB", "lipid17_merged", "phosaa10", "tip3p_HFE_multivalent", "tip3p_standard"]
    small_molecule_forcefield: "openff-2.1.1"
    partial_charges: "am1bccelf10_oe"
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
      - AlchemicalNetwork-47b82fc985880c624d46e880a904b41a jacs_set-bace: ligand_start=CAT-13a, ligand_final=CAT-13c, solvent={'O'}, cofactors=none, protein={'unknown'}
      - AlchemicalNetwork-47b82fc985880c624d46e880a904b41a jacs_set-bace: ligand_start=CAT-13a, ligand_final=CAT-13f, solvent={'O'}, cofactors=none, protein={'unknown'}
      - AlchemicalNetwork-47b82fc985880c624d46e880a904b41a jacs_set-bace: ligand_start=CAT-13a, ligand_final=CAT-13g, solvent={'O'}, cofactors=none, protein={'unknown'}
      - AlchemicalNetwork-47b82fc985880c624d46e880a904b41a jacs_set-bace: ligand_start=CAT-13a, ligand_final=CAT-13i, solvent={'O'}, cofactors=none, protein={'unknown'}
      - AlchemicalNetwork-47b82fc985880c624d46e880a904b41a jacs_set-bace: ligand_start=CAT-13a, ligand_final=CAT-13o, solvent={'O'}, cofactors=none, protein={'unknown'}
      - etc.
  - protocol: "RelativeHybridTopologyProtocol"
    notes: |
      Detailed protocol settings differ:
      - solvation_settings.solvent_padding: 1 -> 1.5
      Applies to 283 edges:
      - AlchemicalNetwork-47b82fc985880c624d46e880a904b41a jacs_set-bace: ligand_start=CAT-13a, ligand_final=CAT-13c, solvent={'O'}, cofactors=none, protein=none
      - AlchemicalNetwork-47b82fc985880c624d46e880a904b41a jacs_set-bace: ligand_start=CAT-13a, ligand_final=CAT-13f, solvent={'O'}, cofactors=none, protein=none
      - AlchemicalNetwork-47b82fc985880c624d46e880a904b41a jacs_set-bace: ligand_start=CAT-13a, ligand_final=CAT-13g, solvent={'O'}, cofactors=none, protein=none
      - AlchemicalNetwork-47b82fc985880c624d46e880a904b41a jacs_set-bace: ligand_start=CAT-13a, ligand_final=CAT-13i, solvent={'O'}, cofactors=none, protein=none
      - AlchemicalNetwork-47b82fc985880c624d46e880a904b41a jacs_set-bace: ligand_start=CAT-13a, ligand_final=CAT-13o, solvent={'O'}, cofactors=none, protein=none
      - etc.


## Rights
- License: CC-BY-4.0
