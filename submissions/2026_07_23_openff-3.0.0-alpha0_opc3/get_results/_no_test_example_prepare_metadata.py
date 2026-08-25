#!/usr/bin/env python
"""Orchestrate metadata preparation for alchemical archive submission.

Uses the Python API directly to invoke the three-step workflow:
1. Pull alchemical network from Alchemiscale
2. Generate computational results
3. Generate submission metadata
"""

import os
import logging
from pathlib import Path

from openfe_benchmarks.scripts.utils import setup_file_logger

# Import the core functions (not the CLI wrappers)
from openfe_benchmarks.scripts._tmp_alchemiscale_gather import run_gather
from openfe_benchmarks.scripts.generate_results_archives import run_generate_results
from openfe_benchmarks.scripts.prepare_metadata_submission import process_network

logger = logging.getLogger(__name__)

SYSTEM_GROUP_SET_KEY = (
    [
        "jacs_set",
        "bace",
        "AlchemicalNetwork-0482bbeceac4470dd4c29afeadfa5825-openff-openff_3_0_0_alpha0_opc3-rbfe_pontibus_jacs_set_bace",
    ],
    [
        "jacs_set",
        "cdk2",
        "AlchemicalNetwork-ea875d9e2896b0e337a17bf950c722ba-openff-openff_3_0_0_alpha0_opc3-rbfe_pontibus_jacs_set_cdk2",
    ],
    [
        "jacs_set",
        "jnk1",
        "AlchemicalNetwork-7420dd6f7be012084483a3d57faa2350-openff-openff_3_0_0_alpha0_opc3-rbfe_pontibus_jacs_set_jnk1",
    ],
    [
        "jacs_set",
        "mcl1",
        "AlchemicalNetwork-21aba16db838ca5833ad036c37ee50d2-openff-openff_3_0_0_alpha0_opc3-rbfe_pontibus_jacs_set_mcl1",
    ],
    [
        "jacs_set",
        "p38",
        "AlchemicalNetwork-ff43514f04705b71bcb834c34c8e51b0-openff-openff_3_0_0_alpha0_opc3-rbfe_pontibus_jacs_set_p38",
    ],
    [
        "jacs_set",
        "ptp1b",
        "AlchemicalNetwork-c7614ad07bf6ffffd3369475e628e20e-openff-openff_3_0_0_alpha0_opc3-rbfe_pontibus_jacs_set_ptp1b",
    ],
    [
        "jacs_set",
        "thrombin",
        "AlchemicalNetwork-febece7a6c1eb4f964a57f994934a31a-openff-openff_3_0_0_alpha0_opc3-rbfe_pontibus_jacs_set_thrombin",
    ],
    [
        "jacs_set",
        "tyk2",
        "AlchemicalNetwork-ea6d43b749172c8d7df19a66bec9838a-openff-openff_3_0_0_alpha0_opc3-rbfe_pontibus_jacs_set_tyk2",
    ],
)
OUTPUT_DIR = "output"

SUBMISSION_ID = "2026_08_05_openff-3.0.0-alpha0_opc3_jacs"
DATE = "2026-08-05"
AUTHOR = "Jennifer A. Clark"
SUMMARY_SUFFIX = (
    "For scripts to generate this network: "
    "github.com/openforcefield/alchemical-benchmark-resources/submissions/2026_07_23_openff-3.0.0-alpha0_opc3/alchemiscale_submission.ipynb"
)
TAGS = "rbfe,benchmark,openfe"
OPENFE_VER = "1.8.0"
OPENMM_VER = "8.2.0"
OFFTOOL_VER = "0.18"
SMALL_MOL_FF = "openff-3.0.0-alpha0"
WATER_MODEL = "opc3.offxml"

if __name__ == "__main__":
    setup_file_logger("log.txt", level=logging.INFO, print_console=True)
    logger.info("Starting metadata preparation workflow")

    # Step 1: Gather network from Alchemiscale
    logger.info("=" * 70)
    logger.info("Step: Pulling alchemical network")
    logger.info("=" * 70)
    for _, _, network_key in SYSTEM_GROUP_SET_KEY:
        if not os.path.isfile(os.path.join(OUTPUT_DIR, f"{network_key}.json.bz2")):
            run_gather(
                network_key=network_key,
                allow_partial=False,
                output=OUTPUT_DIR,
            )
    logger.info("✓ Pulling alchemical network completed successfully\n")

    # Step 2: Generate computational results
    logger.info("=" * 70)
    logger.info("Step: Generating computational_results.json")
    logger.info("=" * 70)
    systems_local = [
        [group, sys_set, os.path.join(OUTPUT_DIR, f"{network_key}.json.bz2")]
        for group, sys_set, network_key in SYSTEM_GROUP_SET_KEY
    ]
    run_generate_results(
        systems=systems_local,
        output_dir=Path(OUTPUT_DIR),
    )
    logger.info("✓ Generating computational_results.json completed successfully\n")

    # Step 3: Generate submission metadata
    logger.info("=" * 70)
    logger.info("Step: Generating submission metadata")
    logger.info("=" * 70)
    process_network(
        systems=systems_local,
        output_dir=Path(OUTPUT_DIR),
        submission_id=SUBMISSION_ID,
        tags=TAGS,
        author=[AUTHOR],
        license="CC-BY-4.0",
        submission_date=DATE,
        summary_suffix=SUMMARY_SUFFIX,
        openfe_version=OPENFE_VER,
        openmm_version=OPENMM_VER,
        openff_toolkit_version=OFFTOOL_VER,
        small_molecule_forcefield=SMALL_MOL_FF,
        forcefields=[SMALL_MOL_FF, WATER_MODEL],
    )
    logger.info("✓ Generating submission metadata completed successfully\n")

    logger.info("=" * 70)
    logger.info("✓ Workflow complete!")
    logger.info("=" * 70)
    logger.info("Check files in this directory:")
    logger.info("  - submission.yaml")
    logger.info("  - zenodo_description.md (do not include in submission)")
