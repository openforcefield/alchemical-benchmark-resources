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
        "AlchemicalNetwork-38e7552634bee5f4d425fe9ed2fb85d9-openff-openff_3_0_0_alpha1b-rbfe_pontibus_jacs_set_bace",
    ],
    [
        "jacs_set",
        "cdk2",
        "AlchemicalNetwork-28ff87e9e98dcc018873a3d0f364c0cd-openff-openff_3_0_0_alpha1b-rbfe_pontibus_jacs_set_cdk2",
    ],
    [
        "jacs_set",
        "jnk1",
        "AlchemicalNetwork-79b5a746219163f999ed27182064a7d0-openff-openff_3_0_0_alpha1b-rbfe_pontibus_jacs_set_jnk1",
    ],
    [
        "jacs_set",
        "mcl1",
        "AlchemicalNetwork-5aca98623a3487f76f1fd7255848a4a9-openff-openff_3_0_0_alpha1b-rbfe_pontibus_jacs_set_mcl1",
    ],
    [
        "jacs_set",
        "p38",
        "AlchemicalNetwork-7337defddce50b480590f8c848143d65-openff-openff_3_0_0_alpha1b-rbfe_pontibus_jacs_set_p38",
    ],
    [
        "jacs_set",
        "ptp1b",
        "AlchemicalNetwork-5a1747bd8d2fec35462d32168df71c4f-openff-openff_3_0_0_alpha1b-rbfe_pontibus_jacs_set_ptp1b",
    ],
    [
        "jacs_set",
        "thrombin",
        "AlchemicalNetwork-8f28971733a4f639c9ba89cba74466f9-openff-openff_3_0_0_alpha1b-rbfe_pontibus_jacs_set_thrombin",
    ],
    [
        "jacs_set",
        "tyk2",
        "AlchemicalNetwork-f8388a2e4aa7e6909e505ae1e61b4e12-openff-openff_3_0_0_alpha1b-rbfe_pontibus_jacs_set_tyk2",
    ],
)
OUTPUT_DIR = "output"

SUBMISSION_ID = "2026-08-05-openff3.0.0-alpha1b_tip3p-jacs"
DATE = "2026-08-05"
AUTHOR = "Jennifer A. Clark"
SUMMARY_SUFFIX = (
    "For scripts to generate this network: "
    "github.com/openforcefield/alchemical-benchmark-resources/submissions/2026_07_15_openff-3.0.0-alpha1b_tip3p/alchemiscale_submission.ipynb"
)
TAGS = "rbfe,benchmark,openfe"
SMALL_MOL_FF = "openff-3.0.0-alpha1b"
WATER_MODEL = "tip3p.offxml"
OPENFE_VER = "1.8.0"
OPENMM_VER = "8.2.0"
OFFTOOL_VER = "0.18"

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
        small_molecule_forcefield=SMALL_MOL_FF,
        forcefields=[SMALL_MOL_FF, WATER_MODEL],
        openfe_version=OPENFE_VER,
        openmm_version=OPENMM_VER,
        openff_toolkit_version=OFFTOOL_VER,
    )
    logger.info("✓ Generating submission metadata completed successfully\n")

    logger.info("=" * 70)
    logger.info("✓ Workflow complete!")
    logger.info("=" * 70)
    logger.info("Check files in this directory:")
    logger.info("  - submission.yaml")
    logger.info("  - zenodo_description.md (do not include in submission)")
