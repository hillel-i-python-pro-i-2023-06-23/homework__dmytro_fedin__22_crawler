import re
from typing import Pattern
from urllib.parse import urlsplit


def get_priority_list(link_list: list[str]) -> list[float]:
    links = link_list
    num_links = len(links)
    links_with_priorities = []

    priority = 1.0
    if len(link_list) > 1:
        step = (1.0 - 0.1) / (num_links - 1)

        for link in links:
            links_with_priorities.append((link, priority))

            priority -= step

    else:
        links_with_priorities = [priority]

    return links_with_priorities


def get_pattern(url: str) -> Pattern[str]:
    full_url = url
    parsed_url = urlsplit(full_url)
    domain = parsed_url.netloc
    domain_parts = domain.split('.')

    if len(domain_parts) > 2:
        domain = '.'.join(domain_parts[1:])

    pattern = re.compile(r"https://([\w-]+\.)?" + re.escape(domain))

    return pattern
