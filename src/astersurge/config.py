"""
AsterSurge Configuration

Centralized configuration management.

Version: 0.1
"""

import os


class Config:
    """Application configuration."""

    APP_NAME = "AsterSurge"
    VERSION = "0.1.0"

    DEFAULT_MODEL = os.getenv(
        "ASTERSURGE_MODEL",
        "echo"
    )

    DEBUG = os.getenv(
        "ASTERSURGE_DEBUG",
        "False"
    ).lower() == "true"

    LOG_LEVEL = os.getenv(
        "ASTERSURGE_LOG_LEVEL",
        "INFO"
    )

    DATA_DIR = os.getenv(
        "ASTERSURGE_DATA_DIR",
        "./data"
    )

    @classmethod
    def as_dict(cls):
        """Return configuration as a dictionary."""

        return {
            "app_name": cls.APP_NAME,
            "version": cls.VERSION,
            "default_model": cls.DEFAULT_MODEL,
            "debug": cls.DEBUG,
            "log_level": cls.LOG_LEVEL,
            "data_dir": cls.DATA_DIR,
        }

    @classmethod
    def print_config(cls):
        """Print current configuration."""

        for key, value in cls.as_dict().items():
            print(f"{key}: {value}")
