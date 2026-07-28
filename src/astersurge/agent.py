"""
AsterSurge Agent

Version: 0.3.0
"""

from .planner import Planner
from .memory import Memory
from .tools import ToolRegistry
from .factory import ProviderFactory
from .prompts import Prompts


class Agent:
    """
    Main AsterSurge Agent.
    """

    def __init__(
        self,
        provider="groq",
        model=None,
    ):
        self.planner = Planner()
        self.memory = Memory()
        self.tools = ToolRegistry()

        self.provider = ProviderFactory.create(
            provider,
            model=model,
        )

    def chat(
        self,
        prompt: str,
        system_prompt=None,
    ):
        """
        Chat directly with the configured LLM.
        """

        self.memory.add("user", prompt)

        response = self.provider.generate(
            prompt,
            system_prompt or Prompts.SYSTEM,
        )

        self.memory.add(
            "assistant",
            response,
        )

        return response

    def run(self, task: str):
        """
        Execute a task.
        """

        plan = self.planner.create_plan(task)

        results = []

        for step in plan:

            tool = self.tools.get(
                step["tool"]
            )

            if tool:

                output = tool.run(task)

            else:

                output = self.chat(task)

            results.append(
                {
                    "step": step["description"],
                    "output": output,
                }
            )

        return {
            "task": task,
            "plan": plan,
            "results": results,
        }

    def history(self):
        return self.memory.history()

    def clear(self):
        self.memory.clear()
