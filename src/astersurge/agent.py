"""
AsterSurge Agent

Minimal agent implementation for AsterSurge.

Version: 0.1
"""

from .planner import Planner
from .memory import Memory
from .tools import ToolRegistry


class Agent:
    """A simple AI agent."""

    def __init__(self):
        self.memory = Memory()
        self.planner = Planner()
        self.tools = ToolRegistry()

    def run(self, task: str):
        """
        Execute a task.

        Parameters
        ----------
        task : str
            User task.

        Returns
        -------
        dict
            Agent execution result.
        """

        self.memory.add("user", task)

        plan = self.planner.create_plan(task)

        results = []

        for step in plan:

            tool = self.tools.get(step["tool"])

            if tool is None:
                output = f"Tool '{step['tool']}' not found."
            else:
                output = tool.run(step["input"])

            results.append(
                {
                    "step": step["description"],
                    "output": output,
                }
            )

        self.memory.add("assistant", str(results))

        return {
            "task": task,
            "plan": plan,
            "results": results,
        }

    def history(self):
        """Return conversation history."""
        return self.memory.history()

    def clear(self):
        """Clear conversation history."""
        self.memory.clear()
