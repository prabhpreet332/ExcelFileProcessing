import logging
import os
import sys


class Constants:
    BASE_DIR_PATH: str = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR_PATH, "data")
    LOGS_DIR = os.path.join(BASE_DIR_PATH, "logs")


class LoggingConfig:
    @staticmethod
    def get_logger():
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        # Create a StreamHandler to log to stdout
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(formatter)

        # Create a FileHandler to log to a file
        if not os.path.exists(Constants.LOGS_DIR):
            os.makedirs(Constants.LOGS_DIR)
        file_handler = logging.FileHandler("./logs/app.log")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)
        return logger


logger = LoggingConfig.get_logger()
