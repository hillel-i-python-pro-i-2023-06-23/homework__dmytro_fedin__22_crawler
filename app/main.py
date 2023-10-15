from source.parser import get_url_list, get_url_depth
from source.crawler import get_urls


def main():
    urls_to_access = get_url_list()

    get_urls(2, urls_to_access)
