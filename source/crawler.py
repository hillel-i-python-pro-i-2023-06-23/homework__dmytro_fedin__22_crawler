import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from .driver import add_to_csv


def get_page_links(url: str) -> list[str]:
    def is_response(current_response: requests.Response) -> bool:
        status_code = current_response.status_code

        if status_code == 403:
            response_status = False
        else:
            response_status = True

        return response_status

    def is_valid_url(url: str) -> bool:
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

    found_urls = []

    response = requests.get(url)

    if is_response(response):
        soup = BeautifulSoup(response.content, "html.parser")

        for url in soup.find_all('a'):
            link_target = url.get('href')

            if is_valid_url(link_target):
                found_urls.append(link_target)

    return found_urls


def get_links(recursion_depth: int, list_of_urls: list[str]):
    if recursion_depth <= 0:
        return

    urls_to_visit = []

    print(f"Got url list to process: {list_of_urls})")

    for url in list_of_urls:
        found_urls = get_page_links(url)

        for found_url in found_urls:
            urls_to_visit.append(found_url)

        add_to_csv(found_urls)

    print(f"Found {len(urls_to_visit)} urls (first is: {urls_to_visit[0]})")
    print(f"Recursions before end: {recursion_depth}")

    get_links(recursion_depth - 1, urls_to_visit)
