import asyncio
from app import main
from source import get_url_depth, get_url_list

urls = get_url_list()
recursion_depth = get_url_depth()

if __name__ == "__main__":
    asyncio.run(main(urls, recursion_depth))
