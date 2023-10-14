from source.parser import get_link_list, get_link_depth
from source.crawler import access_pages


def main():
    links_to_access = get_link_list()
    link_depth = get_link_depth()

    res = access_pages(links_to_access, link_depth)

    # print(res)

