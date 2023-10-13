import logging

# Configure logging settings
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=r"logs/log_file.txt",
    filemode="w",
)


def write_log(msg: str) -> None:
    # Create a logger instance
    logger = logging.getLogger()

    # Write log messages
    logger.info(msg)
