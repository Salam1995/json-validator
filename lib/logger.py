"""logger"""

import sys
import logging


__logger__ = None


def get_logger():

    global __logger__
    if __logger__ is not None:
        return __logger__
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setLevel(logging.INFO)
    consoleHandler.setFormatter(formatter)
    logger.addHandler(consoleHandler)

    __logger__ = logger
    return logger
