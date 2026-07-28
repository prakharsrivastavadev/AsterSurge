"""
AsterSurge Settings

Version: 0.2.0
"""

from dataclasses import dataclass


@dataclass
class Settings:
    """
    Global runtime settings.
    """

    provider: str = "groq"
    model: str = "llama-3.3-70b-versatile"

    temperature: float = 0.2
    max_tokens: int = 1024

    debug: bool = False

    timeout: int = 120

    stream: bool = False

    cache_enabled: bool = True

    plugins_enabled: bool = True

    memory_enabled: bool = True

    events_enabled: bool = True

    log_level: str = "INFO"

    api_host: str = "127.0.0.1"

    api_port: int = 8000
