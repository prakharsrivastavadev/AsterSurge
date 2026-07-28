"""
AsterSurge Tools

Version: 0.3.0
"""

from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path


class BaseTool(ABC):
    """
    Base class for all tools.
    """

    name = "tool"
    description = "Base tool"

    @abstractmethod
    def run(self, *args, **kwargs):
        pass


class EchoTool(BaseTool):

    name = "echo"
    description = "Echo input."

    def run(self, text):
        return text


class DateTimeTool(BaseTool):

    name = "datetime"
    description = "Current date and time."

    def run(self):
        return datetime.now().isoformat()


class CalculatorTool(BaseTool):

    name = "calculator"
    description = "Evaluate arithmetic."

    def run(self, expression):

        allowed = {
            "__builtins__": {}
        }

        return eval(expression, allowed, {})


class FileReaderTool(BaseTool):

    name = "file_reader"
    description = "Read UTF-8 text file."

    def run(self, path):

        path = Path(path)

        if not path.exists():
            raise FileNotFoundError(path)

        return path.read_text(
            encoding="utf-8"
        )


class ToolRegistry:
    """
    Tool registry.
    """

    def __init__(self):

        self._tools = {}

        self.register(EchoTool())
        self.register(DateTimeTool())
        self.register(CalculatorTool())
        self.register(FileReaderTool())

    def register(self, tool):

        self._tools[tool.name] = tool

    def unregister(self, name):

        self._tools.pop(name, None)

    def get(self, name):

        return self._tools.get(name)

    def execute(
        self,
        name,
        *args,
        **kwargs,
    ):

        tool = self.get(name)

        if tool is None:
            raise ValueError(
                f"Unknown tool '{name}'."
            )

        return tool.run(
            *args,
            **kwargs,
        )

    def list(self):

        return sorted(
            self._tools.keys()
        )

    def count(self):

        return len(
            self._tools
        )

    def clear(self):

        self._tools.clear()
