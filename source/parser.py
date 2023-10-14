def get_arguments():
    import argparse

    parser = argparse.ArgumentParser(description="Set the links to process.")
    parser.add_argument(
        "--link_list",
        type=list[str],
        # default=["https://nexus2f.com/"],
        default=["https://www.wikipedia.org/"],
        help="List of links to process.",
    )
    parser.add_argument(
        "--link_depth",
        type=int,
        default="2",
        help="Depth for link processing.",
    )
    arguments = parser.parse_args()

    return arguments


args = get_arguments()


def get_link_list():
    return args.link_list


def get_link_depth():
    return args.link_depth
