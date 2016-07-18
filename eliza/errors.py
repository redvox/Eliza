import logging


class ConfigLoaderError(Exception):
    def __init__(self, message=""):
        logging.getLogger(__name__).error(message)
        self.message = message
