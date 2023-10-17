import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from .driver import add_to_csv
from .logger import write_log


# Get all valid urls from web page by page url
def get_page_urls(url: str) -> list[str]:
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

        for url in soup.find_all("a"):
            link_target = url.get("href")

            if is_valid_url(link_target):
                found_urls.append(link_target)

    return found_urls


# Get urls from all pages pointed in initial url list
def get_urls(recursion_depth: int, list_of_urls: list[str]) -> None:
    if recursion_depth <= 0:
        return

    urls_to_visit = []
    visited_urls = []

    msg = f"Got url list to process: {list_of_urls[:2]} etc.)"
    write_log(msg)

    for url in list_of_urls:
        visited_urls.append(url)

        found_urls = get_page_urls(url)

        [
            urls_to_visit.append(found_url)
            for found_url in found_urls
            if found_url not in visited_urls
        ]

        add_to_csv(found_urls)

    msg = f"Found {len(urls_to_visit)} urls (first is: {urls_to_visit[0]})"
    write_log(msg)

    msg = f"Recursions before end: {recursion_depth}"
    write_log(msg)

    get_urls(recursion_depth - 1, urls_to_visit)
