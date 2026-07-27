"""
AsterSurge Utilities

Version: 0.2.0
"""

import os
import uuid
from datetime import datetime
from pathlib import Path


def generate_id() -> str:
    """
    Generate a unique identifier.
    """
    return str(uuid.uuid4())


def current_timestamp() -> str:
    """
    Return the current UTC timestamp.
    """
    return datetime.utcnow().isoformat()


def ensure_directory(path: str) -> Path:
    """
    Create a directory if it does not exist.
    """
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def file_exists(path: str) -> bool:
    """
    Check whether a file exists.
    """
    return os.path.isfile(path)


def read_text(path: str) -> str:
    """
    Read a UTF-8 text file.
    """
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def write_text(path: str, content: str):
    """
    Write text to a UTF-8 file.
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def append_text(path: str, content: str):
    """
    Append text to a UTF-8 file.
    """
    with open(path, "a", encoding="utf-8") as file:
        file.write(content)


def truncate(text: str, length: int = 120) -> str:
    """
    Truncate long text.
    """
    if len(text) <= length:
        return text

    return text[:length] + "..."


def env(name: str, default=None):
    """
    Read an environment variable.
    """
    return os.getenv(name, default)


def is_empty(value) -> bool:
    """
    Check whether a value is empty.
    """
    return value is None or value == ""


def flatten(items):
    """
    Flatten nested lists.
    """
    result = []

    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result
