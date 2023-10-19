import asyncio
import logging
import aiohttp
import bs4
from typing import TypeAlias
from urllib.parse import urlparse
from source.logger import get_custom_logger

T_URL: TypeAlias = str
T_URLS: TypeAlias = list[T_URL]
T_URLS_AS_SET: TypeAlias = set[T_URL]

T_TEXT: TypeAlias = str


def is_valid_url(url: T_URL) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


async def get_urls_from_text(text: T_TEXT) -> T_URLS_AS_SET:
    soup = bs4.BeautifulSoup(markup=text, features="html.parser")

    urls = set()
    for link_element in soup.find_all("a"):
        url = link_element.get("href")

        if is_valid_url(url):
            urls.add(url)

    return set(urls)


async def make_request(url: T_URL, session: aiohttp.ClientSession, logger: logging.Logger) -> T_TEXT:
    async with session.get(url) as response:
        logger.info(response.status)
        return await response.text()


async def handle_url(url: T_URL, session: aiohttp.ClientSession) -> T_URLS:
    logger = get_custom_logger(name=str(url))

    text = await make_request(url=url, session=session, logger=logger)

    urls_as_set = await get_urls_from_text(text=text)

    return list(urls_as_set)


async def main(urls: T_URLS, depth: int, all_results: list = None):
    if all_results is None:
        all_results = []

    if depth <= 0:
        return all_results

    async with aiohttp.ClientSession() as session:
        tasks = [handle_url(url=url, session=session) for url in urls]

        results = await asyncio.gather(*tasks)

        flattened_results = [item for sublist in results for item in sublist]

        all_results.extend(flattened_results)

        print(all_results)

        await main(urls, depth - 1, all_results)

    return all_results

