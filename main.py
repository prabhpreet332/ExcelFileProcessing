import argparse

import pandas as pd

from configs import Constants, logger


def main():
    pd.read_excel()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Logging configuration with verbosity options"
    )
    args = parser.parse_args()

    logger.info("hello world")
    logger.debug("hello world")
    logger.exception("hello world")
    logger.critical("hello world")
