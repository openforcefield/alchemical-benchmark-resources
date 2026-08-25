# OpenFE RBFE - jacs_set - thrombin, tyk2 - 2026_08_05_ff14sb_openff-3.0.0-alpha1b_tip3p_jacs_tyk2_thrombin

## Overview
RBFE benchmark results prepared from AlchemicalArchive JSON file(s) generated with OpenFE and Alchemiscale.

This submission describes the RBFE benchmark covering the jacs_set benchmark set (thrombin, tyk2)
prepared with ff14SB/lipid17_merged/phosaa10/tip3p_HFE_multivalent/tip3p_standard for proteins and
solvents, and openff-3.0.0-alpha1b with nagl_openff-gnn-am1bcc-1.0.0.pt for ligands, solutes, and
cofactors. The network contains 72 edges across 27 unique ligands. Results are derived from archived
Alchemiscale workflow data. For scripts to generate this network:
github.com/openforcefield/alchemical-benchmark-
resources/submissions/2026_07_23_ff14sb_openff-3.0.0-alpha1b_tip3p/alchemiscale_submission.ipynb

## Repository Reference
This submission is linked from the OpenFE Benchmarks repository:
https://github.com/OpenFreeEnergy/openfe-benchmarks/tree/main/openfe_benchmarks/results/2026_08_05_ff14sb_openff-3.0.0-alpha1b_tip3p_jacs_tyk2_thrombin

## Software Versions
openfe_version: "1.8.0"
openmm_version: "8.2.0"
openff_toolkit_version: "0.18"

## Alchemical Network Keys
  - AlchemicalNetwork-8f0230086292763f9be6b738348307e8: jacs_set/thrombin
  - AlchemicalNetwork-a1efafd1298d735c7032cebe52be9665: jacs_set/tyk2

## Recommended Descriptors
forcefield: ["ff14SB", "lipid17_merged", "phosaa10", "tip3p_HFE_multivalent", "tip3p_standard"]
small_molecule_forcefield: "openff-3.0.0-alpha1b"
partial_charges: nagl_openff-gnn-am1bcc-1.0.0.pt
mapper: "KartografAtomMapper 1.2.0 (LSA)"


## BenchmarkData Provenance
  (from openfe-benchmarks planning script) with associated network key benchmark_data:
  source_repository: https://github.com/OpenFreeEnergy/openfe-benchmarks
  "jacs_set":
    "thrombin": AlchemicalNetwork-8f0230086292763f9be6b738348307e8
    "tyk2": AlchemicalNetwork-a1efafd1298d735c7032cebe52be9665


## Protocol Settings
protocol_settings:
  - protocol: "RelativeHybridTopologyProtocol"
    protocol_library: "openfe"
    timestep: "4.0 fs"
    temperature: "298.15 K"
    pressure: "1 bar"
    forcefields: ["ff14SB", "lipid17_merged", "phosaa10", "tip3p_HFE_multivalent", "tip3p_standard"]
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
      Applies to 36 edges:
      - AlchemicalNetwork-8f0230086292763f9be6b738348307e8 jacs_set-thrombin: ligand_start=1a, ligand_final=1c, solvent={'O'}, cofactors=none, protein={'unknown'}
      - AlchemicalNetwork-8f0230086292763f9be6b738348307e8 jacs_set-thrombin: ligand_start=1a, ligand_final=3b, solvent={'O'}, cofactors=none, protein={'unknown'}
      - AlchemicalNetwork-8f0230086292763f9be6b738348307e8 jacs_set-thrombin: ligand_start=1a, ligand_final=5, solvent={'O'}, cofactors=none, protein={'unknown'}
      - AlchemicalNetwork-8f0230086292763f9be6b738348307e8 jacs_set-thrombin: ligand_start=1b, ligand_final=1a, solvent={'O'}, cofactors=none, protein={'unknown'}
      - AlchemicalNetwork-8f0230086292763f9be6b738348307e8 jacs_set-thrombin: ligand_start=1d, ligand_final=1b, solvent={'O'}, cofactors=none, protein={'unknown'}
      - etc.
  - protocol: "RelativeHybridTopologyProtocol"
    notes: |
      Detailed protocol settings differ:
      - solvation_settings.solvent_padding: 1 -> 1.5
      Applies to 36 edges:
      - AlchemicalNetwork-8f0230086292763f9be6b738348307e8 jacs_set-thrombin: ligand_start=1a, ligand_final=1c, solvent={'O'}, cofactors=none, protein=none
      - AlchemicalNetwork-8f0230086292763f9be6b738348307e8 jacs_set-thrombin: ligand_start=1a, ligand_final=3b, solvent={'O'}, cofactors=none, protein=none
      - AlchemicalNetwork-8f0230086292763f9be6b738348307e8 jacs_set-thrombin: ligand_start=1a, ligand_final=5, solvent={'O'}, cofactors=none, protein=none
      - AlchemicalNetwork-8f0230086292763f9be6b738348307e8 jacs_set-thrombin: ligand_start=1b, ligand_final=1a, solvent={'O'}, cofactors=none, protein=none
      - AlchemicalNetwork-8f0230086292763f9be6b738348307e8 jacs_set-thrombin: ligand_start=1d, ligand_final=1b, solvent={'O'}, cofactors=none, protein=none
      - etc.


## Rights
- License: CC-BY-4.0
