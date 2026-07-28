"""
AsterSurge Configuration

Version: 0.3.0
"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Global configuration.
    """

    APP_NAME = "AsterSurge"
    VERSION = "0.3.0"

    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    PROVIDER = os.getenv(
        "ASTERSURGE_PROVIDER",
        "groq",
    )

    MODEL = os.getenv(
        "ASTERSURGE_MODEL",
        "llama-3.3-70b-versatile",
    )

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    OLLAMA_HOST = os.getenv(
        "OLLAMA_HOST",
        "http://localhost:11434",
    )

    TEMPERATURE = float(
        os.getenv(
            "ASTERSURGE_TEMPERATURE",
            "0.2",
        )
    )

    MAX_TOKENS = int(
        os.getenv(
            "ASTERSURGE_MAX_TOKENS",
            "1024",
        )
    )

    TIMEOUT = int(
        os.getenv(
            "ASTERSURGE_TIMEOUT",
            "120",
        )
    )

    DEBUG = (
        os.getenv(
            "ASTERSURGE_DEBUG",
            "false",
        ).lower()
        == "true"
    )

    LOG_LEVEL = os.getenv(
        "ASTERSURGE_LOG_LEVEL",
        "INFO",
    )

    @classmethod
    def as_dict(cls):
        return {
            "app_name": cls.APP_NAME,
            "version": cls.VERSION,
            "provider": cls.PROVIDER,
            "model": cls.MODEL,
            "temperature": cls.TEMPERATURE,
            "max_tokens": cls.MAX_TOKENS,
            "timeout": cls.TIMEOUT,
            "debug": cls.DEBUG,
            "log_level": cls.LOG_LEVEL,
        }

    @classmethod
    def get(cls, key, default=None):
        return getattr(cls, key, default)
