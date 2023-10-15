from source.parser import get_link_list, get_link_depth
from source.crawler import get_links



def main():

    urls_to_access = get_link_list()

    get_links(2, urls_to_access)


