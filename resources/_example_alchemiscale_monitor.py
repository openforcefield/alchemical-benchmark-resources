import pathlib
import click

from alchemiscale import AlchemiscaleClient, Scope, ScopedKey
from gufe import AlchemicalNetwork
import logging

logger = logging.getLogger(__name__)


def _configure_example_logging(level=logging.INFO):
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
    )
    # Attach to this module's logger so output appears when running the example
    logger.addHandler(handler)
    logger.setLevel(level)
    # Optionally enable package-wide logs:
    logging.getLogger("openfe_benchmarks").setLevel(level)


@click.command()
@click.option(
    "--inputs",
    type=click.Path(dir_okay=True, file_okay=True, exists=True, path_type=pathlib.Path),
    help="Path to the directory containing the alchemical network json files or a single json file which contain the network keys.",
    default=None,
)
@click.option(
    "--org",
    type=str,
    help="Organization name used to build the scope to check can not be used with --inputs.",
    default=None,
)
@click.option(
    "--campaign",
    type=str,
    help="Campaign name used to build the scope to check can not be used with --inputs.",
    default=None,
)
@click.option(
    "--project",
    type=str,
    help="Project name used to build the scope to check can not be used with --inputs.",
    default=None,
)
@click.option(
    "--restart",
    is_flag=True,
    help="Whether to restart any existing submissions found for the given scope which have an error status.",
    default=False,
)
@click.option(
    "--show-errors-only",
    is_flag=True,
    help="Whether to only show submissions with error status for the given scope.",
    default=False,
)
@click.option(
    "--cancel",
    is_flag=True,
    help="Whether to cancel any existing submissions found for the given scope which have an error status instead of restarting them.",
    default=False,
)
def main(inputs, org, campaign, project, restart, show_errors_only, cancel):
    """
    Check the status of Alchemiscale submissions for the given scope and optionally restart any tasks with an error status.

    Examples
    --------
    - Check the status of all submissions for the openfe organization and my_campaign campaign:
    ```
    python _example_alchemiscale_monitor.py --org openfe --campaign my_campaign
    ```
    - Check the status of all submissions for a specific project:
    ```
    python _example_alchemiscale_monitor.py --org openfe --campaign my_campaign --project my_project
    ```
    - Check the status of submissions for networks found in a specific directory and restart any with an error status:
    ```
    python _example_alchemiscale_monitor.py --inputs /path/to/networks --restart
    ```

    Notes
    -----
    - We assume your alchemiscale login details are set in your environment variables.
    - If inputs is a dir then we search for all JSON files called *submitted_alchemicalnetwork.json and check the status of the submissions for each network found.
    """
    # we can not use scope with inputs
    if inputs is not None and (
        org is not None or campaign is not None or project is not None
    ):
        raise ValueError(
            "Scope searching (org, campaign, project) can not be used when --inputs is provided these are mutually exclusive."
        )
    _configure_example_logging()
    client = AlchemiscaleClient(api_url="https://api.alchemiscale.org")
    # Load the alchemical networks from the input path
    if inputs is not None:
        if inputs.is_file():
            network_keys = [
                ScopedKey.from_str(AlchemicalNetwork.from_json(inputs.as_posix()).name)
            ]
        else:
            network_keys = []
            for json_file in inputs.rglob("*submitted_alchemicalnetwork.json"):
                logger.info(f"Loading network from {json_file}")
                network_keys.append(
                    ScopedKey.from_str(
                        AlchemicalNetwork.from_json(json_file.as_posix()).name
                    )
                )
    else:
        # use the scope to query for network keys
        query_scope = Scope(org=org, campaign=campaign, project=project)
        logger.info(f"Querying Alchemiscale for submissions with scope: {query_scope}")
        network_keys = client.query_networks(scope=query_scope)

    logger.info(f"Number of networks found: {len(network_keys)}")
    for network_key in network_keys:
        logger.info(f"Checking status for network with key: {network_key}")
        network_status = client.get_network_status(network=network_key)

        errors = network_status.get("error", 0)
        if cancel:
            # pull all running and waiting tasks and cancel them
            running_tasks = client.get_network_tasks(
                network=network_key, status="running"
            )
            waiting_tasks = client.get_network_tasks(
                network=network_key, status="waiting"
            )
            tasks_to_cancel = running_tasks + waiting_tasks
            if len(tasks_to_cancel) > 0:
                logger.info(
                    f"Cancelling {len(tasks_to_cancel)} running/waiting tasks for network {network_key} ...."
                )
                cancelled_tasks = client.set_tasks_status(
                    tasks=tasks_to_cancel, status="deleted"
                )
                logger.info(
                    f"Cancelled {len(cancelled_tasks)} tasks for network {network_key}."
                )

        if errors > 0:
            logger.warning(
                f"Network {network_key} has {errors} tasks with error status."
            )
            errored_tasks = client.get_network_tasks(
                network=network_key, status="error"
            )
            if show_errors_only:
                error_data = []
                for task in errored_tasks:
                    for error_result in client.get_task_failures(task):
                        for protocol_failure in error_result.protocol_unit_failures:
                            error_data.append(
                                {
                                    "task_id": task,
                                    "exception": protocol_failure.exception,
                                    "traceback": protocol_failure.traceback,
                                    "unit_key": protocol_failure.key,
                                }
                            )
                for error in error_data:
                    logger.error(
                        f"Task {error['task_id']} failed with exception: {error['exception']}\nTraceback: {error['traceback']}\nUnit key: {error['unit_key']}"
                    )

            elif restart:
                logger.info(
                    f"Restarting tasks with error status for network {network_key} ...."
                )
                restarted_tasks = client.set_tasks_status(
                    tasks=errored_tasks, status="waiting"
                )
                logger.info(
                    f"Restarted {len(restarted_tasks)} tasks for network {network_key}."
                )


if __name__ == "__main__":
    main()
