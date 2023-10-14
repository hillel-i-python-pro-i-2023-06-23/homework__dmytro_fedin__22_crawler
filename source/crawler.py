from queue import PriorityQueue

import requests
from bs4 import BeautifulSoup
import queue
import re
import time
import random

from .driver import get_priority_list, get_pattern


def access_pages(link_list: list[str], link_depth: int):
    visited_urls = []
    failed_access_urls = []
    urls = queue.PriorityQueue()

    priority_list = get_priority_list(link_list)

    [urls.put((priority, link)) for priority, link in zip(priority_list, link_list)]

    while not urls.empty():
        _, current_url = urls.get()

        response = requests.get(current_url)

        if response.status_code == 403:
            print(f"Got status_code {response.status_code} for {current_url}")
            failed_access_urls.append(current_url)

            continue

        else:
            print(f"Got status_code {response.status_code} for {current_url}")

            soup = BeautifulSoup(response.content, "html.parser")

            visited_urls.append(current_url)

            link_elements = soup.select("a[href]")

            for link_element in link_elements:
                url = link_element['href']

                pattern = get_pattern(current_url)

                if re.match(pattern, url):

                    print(f"For link {link_element.name} url is {url}")
                    if url not in visited_urls and url not in [item[1] for item in urls.queue]:
                        priority_score = 1
                        urls.put((priority_score, url))

        time.sleep(1)
