def get_arguments():
    import argparse

    parser = argparse.ArgumentParser(description="Set the links to process.")
    parser.add_argument(
        "--link_list",
        type=list[str],
        default=["https://www.example.com/", "https://www.google.com/"],
        # default=["https://www.google.com/"],
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


def get_url_list():
    return args.link_list


def get_url_depth():
    return args.link_depth
