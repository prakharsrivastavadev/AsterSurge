"""
AsterSurge

Open-source AI infrastructure for building intelligent software.

Version: 0.3.0
"""

from .agent import Agent
from .planner import Planner
from .memory import Memory
from .tools import (
    BaseTool,
    ToolRegistry,
)
from .models import (
    Model,
    ModelManager,
)
from .config import Config
from .factory import ProviderFactory
from .plugins import (
    Plugin,
    PluginManager,
)
from .logger import Logger
from .cache import Cache
from .storage import (
    Storage,
    MemoryStorage,
)
from .events import EventBus
from .registry import Registry
from .router import Router
from .executor import Executor
from .validators import Validator
from .scheduler import Scheduler
from .serializer import Serializer
from .prompts import Prompts
from .loader import Loader
from .settings import Settings

__version__ = Config.VERSION

__all__ = [
    "Agent",
    "Planner",
    "Memory",
    "BaseTool",
    "ToolRegistry",
    "Model",
    "ModelManager",
    "Config",
    "ProviderFactory",
    "Plugin",
    "PluginManager",
    "Logger",
    "Cache",
    "Storage",
    "MemoryStorage",
    "EventBus",
    "Registry",
    "Router",
    "Executor",
    "Validator",
    "Scheduler",
    "Serializer",
    "Prompts",
    "Loader",
    "Settings",
]
