import pathlib
import click

from alchemiscale import AlchemiscaleClient, Scope
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
    help="Path to the directory containing the alchemical network json files or a single json file.",
)
@click.option(
    "--output",
    type=click.Path(dir_okay=True, file_okay=False, path_type=pathlib.Path),
    help="Path to the directory where the Alchemiscale submissions will be saved.",
)
@click.option(
    "--org",
    type=str,
    help="Organization name for the Alchemiscale submission.",
    default="openfe",
)
@click.option(
    "--campaign",
    type=str,
    help="Campaign name for the Alchemiscale submission.",
    required=True,
)
@click.option(
    "--project",
    type=str,
    help="Project name for the Alchemiscale submission if many networks the system_group system_name will be used.",
    required=False,
    default=None,
)
@click.option(
    "--repeats", type=int, help="Number of repeats for each submission.", default=3
)
def main(inputs, output, org, campaign, project, repeats):
    """
    We assume your alchemiscale login details are set in your environment variables.

    Notes
    -----
    - The method will recursively search for all JSON files called *_alchemicalnetwork.json in the input directory unless a single JSON file is provided.
    - The output network JSON files will be named {system_group}_{system_name}_submitted_alchemicalnetwork.json and saved in the output directory.
    - The script assumes that all edges have a mapping and that the system_group and system_name annotations are present in the mapping.

    """
    _configure_example_logging()
    client = AlchemiscaleClient(api_url="https://api.alchemiscale.org")
    # Load the alchemical networks from the input path
    if inputs.is_file():
        networks = [AlchemicalNetwork.from_json(inputs.as_posix())]
    else:
        networks = []
        for json_file in inputs.rglob("*_alchemicalnetwork.json"):
            logger.info(f"Loading network from {json_file}")
            networks.append(AlchemicalNetwork.from_json(json_file.as_posix()))

    logger.info(f"Number of networks found: {len(networks)}")
    if len(networks) > 1 and project is not None:
        raise ValueError(
            "A project name should not be provided when submitting multiple networks, the system_group and system_name will be used to create unique project names for each network."
        )

    # Create submissions for each network
    output_dir = pathlib.Path(output)
    output_dir.mkdir(parents=True, exist_ok=True)

    for network in networks:
        # Create a unique project name if not provided
        if project is None:
            edge = list(network.edges)[0]
            system_group = edge.mapping.annotations["system_group"]
            system_name = edge.mapping.annotations["system_name"]
            project = f"{system_group}_{system_name}"

        scope = Scope(org=org, campaign=campaign, project=project)

        logger.info(f"Submitting network with scope: {scope}")
        network_key = client.create_network(network=network, scope=scope)
        logger.info(f"Created network with key: {network_key}")
        # save the network to file with the key as the name
        network_output_path = output_dir / f"{project}_submitted_alchemicalnetwork.json"
        new_network = AlchemicalNetwork(edges=network.edges, name=str(network_key))
        new_network.to_json(network_output_path.as_posix())

        # now action the network
        tasks = []
        for tf_sk in client.get_network_transformations(network_key):
            tasks.extend(client.create_tasks(tf_sk, count=repeats))

        # now action the tasks to make sure they are picked up by compute
        actioned_tasks = client.action_tasks(tasks, network_key)
        logger.info(f"Actioned {len(actioned_tasks)} tasks for network {network_key}")
        # get the status of the network
        client.get_network_status(network_key)


if __name__ == "__main__":
    main()
