"""
AsterSurge Logging

Version: 0.2.0
"""

import logging


class Logger:
    """
    Simple logging wrapper.
    """

    def __init__(
        self,
        name="AsterSurge",
        level=logging.INFO,
    ):
        self.logger = logging.getLogger(name)

        if not self.logger.handlers:

            handler = logging.StreamHandler()

            formatter = logging.Formatter(
                "[%(asctime)s] %(levelname)s - %(message)s"
            )

            handler.setFormatter(formatter)

            self.logger.addHandler(handler)

        self.logger.setLevel(level)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
