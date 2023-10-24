import csv
import os
from datetime import datetime


async def add_to_csv(item: str) -> None:
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, "logs/urls.csv")

    with open(file_path, "a") as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow([item])


def get_current_time() -> datetime:
    return datetime.now()


def get_time_delta(start_time: datetime, end_time: datetime) -> str:
    execution_time = end_time - start_time

    return f"{execution_time.total_seconds():.1f}"
