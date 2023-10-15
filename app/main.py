from source.parser import get_url_list, get_url_depth
from source.crawler import get_urls
from source.logger import write_log


def main():
    write_log("New run")

    urls_to_access = get_url_list()

    get_urls(recursion_depth=2, list_of_urls=urls_to_access)
