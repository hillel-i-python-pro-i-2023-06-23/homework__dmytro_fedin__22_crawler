from source.parser import get_link_list, get_link_depth
from source.crawler import get_page_links
from source.driver import add_to_csv


def main():
    visited_links = []
    links_to_visit = []

    links_to_access = get_link_list()

    for link in links_to_access:

        visited_links.append(link)

        derived_links = get_page_links(link)

        links_to_visit.append(derived_links)

        add_to_csv(derived_links)


