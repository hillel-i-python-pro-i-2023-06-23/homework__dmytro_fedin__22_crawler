from source.parser import get_url_list, get_url_depth
from source.crawler import get_urls
from source.logger import write_log
from source.driver import get_current_time, get_time_delta


def main():
    write_log("New run")
    start_time = get_current_time()

    urls_to_access = get_url_list()

    get_urls(recursion_depth=2, list_of_urls=urls_to_access)

    end_time = get_current_time()
    time_delta = get_time_delta(start_time=start_time, end_time=end_time)
    msg = f"Execution time is {time_delta} second(s)"
    write_log(msg)

    print(msg)
