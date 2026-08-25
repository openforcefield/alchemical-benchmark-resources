# OpenFE ASFE - solvation_set - freesolv - 2026-08-06-openff-2.3.0-solvation_set_freesolv

## Overview
ASFE benchmark results prepared from AlchemicalArchive JSON file(s) generated with OpenFE and Alchemiscale.

This submission describes the ASFE benchmark covering the solvation_set benchmark set (freesolv)
prepared with openff-2.3.0/tip3p for solvents and nagl_openff-gnn-am1bcc-1.0.0.pt for solutes and
cofactors. The archive contains 603 edges across 603 unique solutes and 1 unique solvents. Results
are derived from archived Alchemiscale workflow data. This is the full freesolv set that is
parametrizable by OpenFF-2.3.0, submitted before the development of OpenFF subsets.

## Repository Reference
This submission is linked from the OpenFE Benchmarks repository:
https://github.com/OpenFreeEnergy/openfe-benchmarks/tree/main/openfe_benchmarks/results/2026-08-06-openff-2.3.0-solvation_set_freesolv

## Software Versions
openfe_version: "1.8.0"
openmm_version: "8.2.0"
openff_toolkit_version: "0.18"

## Alchemical Network Keys
  - AlchemicalNetwork-55961080ba1805b112aff83fca84b15f: solvation_set/freesolv

## Recommended Descriptors
partial_charges: nagl_openff-gnn-am1bcc-1.0.0.pt

forcefield: ["openff-2.3.0", "tip3p"]



## BenchmarkData Provenance (from openfe-benchmarks planning script) with associated network key 
benchmark_data:
  source_repository: https://github.com/OpenFreeEnergy/openfe-benchmarks
  "solvation_set":
    "freesolv": AlchemicalNetwork-55961080ba1805b112aff83fca84b15f


## Protocol Settings
protocol_settings:
  - protocol: "ASFEProtocol"
    protocol_library: "pontibus"
    timestep: "4.0 fs"
    temperature: "298.15 K"
    pressure: "1 bar"
    forcefields: ["openff-2.3.0", "tip3p"]
    small_molecule_forcefield: ""
    partial_charges: "nagl_openff-gnn-am1bcc-1.0.0.pt"
    equilibration_time: 
    production_time: 
    vacuum_equilibration_time: "500.00000000000006 ps"
    vacuum_production_time: "2.0 ns"
    solvent_equilibration_time: "1.0 ns"
    solvent_production_time: "10.0 ns"
    lambda_functions: ""
    lambda_windows: ""
    lambda_schedule: ""
    notes: "Applies to all edges"


## Rights
- License: CC-BY-4.0
