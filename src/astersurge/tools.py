"""
AsterSurge Tools

Built-in tools and tool registry.

Version: 0.1
"""

from datetime import datetime
import os


class BaseTool:
    """Base class for all tools."""

    name = "base"
    description = "Base tool"

    def run(self, input_data):
        raise NotImplementedError


class EchoTool(BaseTool):
    name = "echo"
    description = "Returns the provided input."

    def run(self, input_data):
        return input_data


class DateTimeTool(BaseTool):
    name = "datetime"
    description = "Returns the current date and time."

    def run(self, input_data=None):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class CalculatorTool(BaseTool):
    name = "calculator"
    description = "Evaluates basic mathematical expressions."

    def run(self, input_data):

        expression = input_data.replace("calculate", "").strip()

        try:
            allowed = {
                "__builtins__": {}
            }

            result = eval(expression, allowed, {})

            return result

        except Exception as e:
            return f"Calculation Error: {e}"


class FileReaderTool(BaseTool):
    name = "file_reader"
    description = "Reads a local text file."

    def run(self, input_data):

        path = input_data.replace("read", "").replace("open", "").replace("file", "").strip()

        if not os.path.exists(path):
            return "File not found."

        try:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()

        except Exception as e:
            return str(e)


class ToolRegistry:
    """Registry for built-in tools."""

    def __init__(self):

        self.tools = {
            "echo": EchoTool(),
            "datetime": DateTimeTool(),
            "calculator": CalculatorTool(),
            "file_reader": FileReaderTool(),
        }

    def register(self, tool):

        self.tools[tool.name] = tool

    def get(self, name):

        return self.tools.get(name)

    def list_tools(self):

        return list(self.tools.keys())
