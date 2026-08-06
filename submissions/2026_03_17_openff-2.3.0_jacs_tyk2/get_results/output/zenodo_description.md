# OpenFE RBFE - jacs_set - tyk2 - 2026-06-22-tyk2-alchemicalarchive-test
## Overview

RBFE benchmark results prepared from AlchemicalArchive JSON file(s) generated with OpenFE and Alchemiscale.

This submission describes the RBFE benchmark covering the jacs_set benchmark set (tyk2) prepared
with ff14SB/phosaa10/tip3p_HFE_multivalent/tip3p_standard for proteins and solvents, and
openff-2.3.0 with nagl_openff-gnn-am1bcc-1.0.0.pt for ligands, solutes, and cofactors. The network
contains 44 edges across 16 unique ligands. Results are derived from archived Alchemiscale workflow
data. This subset of the JACS set is meant to provide an example of an alchemical archive submission
and provide an indication of the variability in results. For scripts to generate this network:
github.com/openforcefield/alchemical-benchmark-
resources/submissions/2026_03_17_openff-2.3.0_jacs_tyk2/alchemiscale_submission.ipynb

## Repository Reference
This submission is linked from the OpenFE Benchmarks repository:
https://github.com/OpenFreeEnergy/openfe-benchmarks/tree/main/openfe_benchmarks/results/2026-06-22-tyk2-alchemicalarchive-test

## Software Versions

openfe_version: 1.8.0
openmm_version: 8.2.0
openff_toolkit_version: 0.18

## Alchemical Network Keys:
  - AlchemicalNetwork-2dd5d032b0228c7474eda50d8e064c2d: jacs_set/tyk2

## Recommended Descriptors

forcefield: ["ff14SB", "phosaa10", "tip3p_HFE_multivalent", "tip3p_standard"]
small_molecule_forcefield: "openff-2.3.0"
partial_charges: nagl_openff-gnn-am1bcc-1.0.0.pt
mapper: "KartografAtomMapper 1.2.0 (LSA)"


# BenchmarkData provenance (from openfe-benchmarks planning script) with associated network key
benchmark_data:
  source_repository: https://github.com/OpenFreeEnergy/openfe-benchmarks
  "jacs_set":
    "tyk2": AlchemicalNetwork-2dd5d032b0228c7474eda50d8e064c2d


## Protocol Settings

protocol_settings:
  - protocol: "RelativeHybridTopologyProtocol"
    timestep: "4.0 fs"
    temperature: "298.15 K"
    pressure: "1 bar"
    forcefields: ["ff14SB", "phosaa10", "tip3p_HFE_multivalent", "tip3p_standard"]
    small_molecule_forcefield: "openff-2.3.0"
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
      Applies to 22 edges:
      - AlchemicalNetwork-2dd5d032b0228c7474eda50d8e064c2d jacs_set-tyk2: ligand_start=ejm_31, ligand_final=ejm_42, solvent={'O'}, cofactors=none, protein=none
      - AlchemicalNetwork-2dd5d032b0228c7474eda50d8e064c2d jacs_set-tyk2: ligand_start=ejm_31, ligand_final=ejm_44, solvent={'O'}, cofactors=none, protein=none
      - AlchemicalNetwork-2dd5d032b0228c7474eda50d8e064c2d jacs_set-tyk2: ligand_start=ejm_31, ligand_final=ejm_45, solvent={'O'}, cofactors=none, protein=none
      - AlchemicalNetwork-2dd5d032b0228c7474eda50d8e064c2d jacs_set-tyk2: ligand_start=ejm_31, ligand_final=ejm_46, solvent={'O'}, cofactors=none, protein=none
      - AlchemicalNetwork-2dd5d032b0228c7474eda50d8e064c2d jacs_set-tyk2: ligand_start=ejm_31, ligand_final=ejm_48, solvent={'O'}, cofactors=none, protein=none
      - etc.
  - protocol: "RelativeHybridTopologyProtocol"
    notes: |
      Detailed protocol settings differ:
      - solvation_settings.solvent_padding: 1.5 -> 1
      Applies to 22 edges:
      - AlchemicalNetwork-2dd5d032b0228c7474eda50d8e064c2d jacs_set-tyk2: ligand_start=ejm_31, ligand_final=ejm_42, solvent={'O'}, cofactors=none, protein={'unknown'}
      - AlchemicalNetwork-2dd5d032b0228c7474eda50d8e064c2d jacs_set-tyk2: ligand_start=ejm_31, ligand_final=ejm_44, solvent={'O'}, cofactors=none, protein={'unknown'}
      - AlchemicalNetwork-2dd5d032b0228c7474eda50d8e064c2d jacs_set-tyk2: ligand_start=ejm_31, ligand_final=ejm_45, solvent={'O'}, cofactors=none, protein={'unknown'}
      - AlchemicalNetwork-2dd5d032b0228c7474eda50d8e064c2d jacs_set-tyk2: ligand_start=ejm_31, ligand_final=ejm_46, solvent={'O'}, cofactors=none, protein={'unknown'}
      - AlchemicalNetwork-2dd5d032b0228c7474eda50d8e064c2d jacs_set-tyk2: ligand_start=ejm_31, ligand_final=ejm_48, solvent={'O'}, cofactors=none, protein={'unknown'}
      - etc.


## Rights
- License: CC-BY-4.0
