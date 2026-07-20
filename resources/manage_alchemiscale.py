import os
import pathlib
from typing import Optional
import csv

from tqdm import tqdm
import numpy as np

from openff.units import unit
import openfe
from alchemiscale import AlchemiscaleClient, Scope


def submit_alchemiscale(
    org_scope: str,
    scope_name_campaign: str,
    base_scope_name_project: str,
):
    """
    Submit and action an AlchemicalNetwork on Alchemiscale.

    Parameters
    ----------
    org_scope : str
      The organization Scope name.
    scope_name_campaign : str
      The campaign Scope name.
    base_scope_name_project : str
      The project Scope name.
    """
    # Get the alchemiscale bits
    user_id = os.environ["ALCHEMISCALE_ID"]
    user_key = os.environ["ALCHEMISCALE_KEY"]
    asc = AlchemiscaleClient("https://api.alchemiscale.org", user_id, user_key)

    for charge_method in ["elf10"]:
        forcefield = "openff-2.2.1"
        network_filename = (
            f"AlchemicalNetworks/openff-2.2.1_{charge_method}_alchemical_network.json"
        )
        print(network_filename)
        # Get the alchemical network
        alchemical_network = openfe.AlchemicalNetwork.from_json(network_filename)

        # Set the scope for the transformation
        ffname = forcefield.replace("-", "_").replace(".", "_")
        scope_name_project = f"{ffname}_{charge_method}_{base_scope_name_project}"
        scope = Scope(org_scope, scope_name_campaign, scope_name_project)
        print(f"Scope is set to: {scope}")

        # Create a network and get a scope key
        an_sk = asc.create_network(alchemical_network, scope)

        # store the scoped key
        with open(f"{forcefield}_{charge_method}.key", "w") as f:
            f.write(str(an_sk))

        # action out tasks
        repeats = 3
        print(
            f"Actioning {repeats} repeats for {len(alchemical_network.edges)} transformation"
        )
        for transform in tqdm(alchemical_network.edges):
            transform_sk = asc.get_scoped_key(transform, scope)
            tasks = asc.create_tasks(transform_sk, count=repeats)
            asc.action_tasks(tasks, an_sk)

        # check what the network status looks like
        asc.get_network_status(an_sk)


def restart_failures(restart):
    """
    Monitor a network of transformation tasks and
    optionally restart failed tasks.

    Parameters
    ----------
    restart : bool
      Whether or not to attempt to restart failed tasks.
    """
    # Get the alchemiscale bits
    user_id = os.environ["ALCHEMISCALE_ID"]
    user_key = os.environ["ALCHEMISCALE_KEY"]
    asc = AlchemiscaleClient("https://api.alchemiscale.org", user_id, user_key)

    keys = [p for p in pathlib.Path(".").glob("*.key")]

    for key in keys:
        with open(key, "r") as f:
            network_sk = f.read()

        asc.get_network_status(network_sk)

        if restart:
            err_tasks = asc.get_network_tasks(network_sk, status="error")
            print(f"Number of errored tasks found: {len(err_tasks)}")
            if len(err_tasks) > 0:
                print("Will attempt to restart tasks")
                asc.set_tasks_status(err_tasks, "waiting")

                print("Printing new network status")
                asc.get_network_status(network_sk)
            else:
                print("No errored tasks were found, no further action")


def _scan_components(system):
    comps = system.components.values()
    if any([isinstance(comp, openfe.ProteinComponent) for comp in comps]):
        return "complex"
    elif any([isinstance(comp, openfe.SolventComponent) for comp in comps]):
        return "solvent"
    else:
        return "vacuum"


def _get_average_and_stdevs(estimates) -> tuple[unit.Quantity, unit.Quantity]:
    """
    Get the average and stdev from a series
    of estimates.

    Parameters
    ----------
    estimates : list[unit.Quantity]
      A list of dG estimates for each repeat.

    Returns
    -------
    avg : unit.Quantity
      The average dG value.
    stdev : unit.Quantity
      The standard deviation of all estimates.
    """
    u = estimates[0].u
    dGs = [i.to(u).m for i in estimates]

    avg = np.average(dGs) * u
    stdev = np.std(dGs) * u

    return avg, stdev


def _process_dagresults(  # Note Used
    dag_results,
) -> tuple[Optional[unit.Quantity], Optional[unit.Quantity]]:
    """
    Process a list of ProtocolDAGResults and get the average dG and error.

    If the list is empty, returns ``None, None``.

    Parameters
    ----------
    dag_results : list[ProtocolDAGResult]
      A list of ProtocolDAGResult for a transformation.

    Returns
    -------
    dG : Optional[unit.Quantity]
      The average free energy for a transformation.
    err : Optional[unit.Quantity]
      The standard deviation in the free energy estimate between multiple
      repeats.
    """

    if len(dag_results) == 0:
        return None, None

    dG = {"solvent": [], "vacuum": []}

    for dresult in dag_results:
        for result in dresult.protocol_unit_results:
            if result.ok():
                dG[result.outputs["simtype"]].append(result.outputs["unit_estimate"])

    vac_dG, vac_err = _get_average_and_stdevs(dG["vacuum"])
    sol_dG, sol_err = _get_average_and_stdevs(dG["solvent"])

    dG = vac_dG - sol_dG
    err = np.sqrt(vac_err**2 + sol_err**2)

    return dG, err


def _write_results(results, results_file) -> None:  # Note Used
    """
    Write out a tab separate list of results for each transformation.

    If the transformation results are not present, writes ``None``.

    Parameters
    ----------
    results : dict[str, list[unit.Quantity]]
      A dictionary keyed by transformation names with each entry
      containing a list of dG and stdev values for each transformation.
    results_file : pathlib.Path
      A path to the file where the results will be written.
    """
    with open(results_file, "w") as f:
        f.write("molecule\tdG (kcal/mol)\tstdev (kcal/mol)\n")
        for r in results.keys():
            if results[r][0] is None:
                f.write(f"{r}\tNone\tNone\n")
            else:
                f.write(f"{r}\t{results[r][0].m}\t{results[r][1].m}\n")


def gether_transformation_results():
    """
    Gather transformation results.

    Parameters
    ----------
    scope_key : pathlib.Path
      A path to a serialized ScopeKey
    user_id : Optional[str]
      A string for a user ID, if undefined will
      fetch from the environment variable ALCHEMISCALE_ID.
    user_key: Optional[str]
      A string for the user key, if underfined will
      fetch from the environment variable ALCHEMISCALE_KEY.
    """
    # Get the alchemiscale bits
    user_id = os.environ["ALCHEMISCALE_ID"]
    user_key = os.environ["ALCHEMISCALE_KEY"]
    asc = AlchemiscaleClient("https://api.alchemiscale.org", user_id, user_key)

    scope_keys = [pathlib.Path("openff-2.2.1_elf10.key")]

    for scope_key in scope_keys:
        # Read in the ScopeKey
        with open(scope_key, "r") as f:
            network_sk = f.read()

        # Loop through each transformation and get the results
        results = dict()  # The results container
        for transf_sk in asc.get_network_transformations(network_sk):
            transf = asc.get_transformation(transf_sk)
            dag_results = asc.get_transformation_results(transf_sk)
            mapping = transf.mapping
            nameA = mapping.componentA.name
            nameB = mapping.componentB.name
            runtype = _scan_components(transf.stateA)

            if dag_results is not None:
                if f"{nameA}_{nameB}" in results.keys():
                    results[f"{nameA}_{nameB}"][runtype] = dag_results
                else:
                    results[f"{nameA}_{nameB}"] = {
                        runtype: dag_results,
                        "molA": nameA,
                        "molB": nameB,
                    }

        with open(f"results/{scope_key.name.strip('.key')}.ddG", "w") as output_file:
            writer = csv.writer(output_file, delimiter="\t", lineterminator="\n")
            writer.writerow(
                [
                    "ligand_i",
                    "ligand_j",
                    "DDG(i->j) (kcal/mol)",
                    "uncertainty (kcal/mol)",
                ]
            )

            for key in results:
                if (
                    "complex" in results[key].keys()
                    and "solvent" in results[key].keys()
                ):
                    estimate = (
                        results[key]["complex"].get_estimate()
                        - results[key]["solvent"].get_estimate()
                    ).m
                    err = np.sqrt(
                        results[key]["complex"].get_uncertainty() ** 2
                        + results[key]["solvent"].get_uncertainty() ** 2
                    ).m
                    molA = results[key]["molA"]
                    molB = results[key]["molB"]
                    writer.writerow([molA, molB, round(estimate, 2), round(err, 2)])
