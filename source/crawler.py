import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


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
