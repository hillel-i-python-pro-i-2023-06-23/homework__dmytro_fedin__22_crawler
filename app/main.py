import asyncio
import aiohttp
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from source.parser import get_url_list, get_url_depth


async def fetch_url(session, url, depth):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            content = await response.text()

        return (depth, url, content)
    except Exception as e:
        return None


async def process_page(session, queue, url, depth):

    visited_urls = []

    page = await fetch_url(session, url, depth)
    if page is None:
        return

    depth, url, content = page

    soup = BeautifulSoup(content, "html.parser")

    for link in soup.find_all("a", href=True):
        new_url = urljoin(url, link["href"])
        if new_url not in visited_urls:
            print(new_url)
            visited_urls.append(new_url)

            await queue.put((depth + 1, new_url))


async def main():
    initial_urls = get_url_list()
    max_depth = get_url_depth()

    queue = asyncio.Queue()

    for url in initial_urls:
        await queue.put((1, url))

    async with aiohttp.ClientSession() as session:
        while not queue.empty():
            depth, url = await queue.get()
            if depth > max_depth:
                print(f"max depth {max_depth} reached")
                break

            print(f"Run with depth {depth}")

            await process_page(
                session=session,
                queue=queue,
                url=url,
                depth=depth,
            )
