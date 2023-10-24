import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=r"logs/log_file.txt",
    filemode="a",
)


def write_log(msg: str) -> None:
    logger = logging.getLogger()

    logger.info(msg)
