"""
AsterSurge Planner

Minimal task planner for AsterSurge.

Version: 0.1
"""


class Planner:
    """Simple rule-based planner."""

    def create_plan(self, task: str):
        """
        Convert a user task into executable steps.

        Parameters
        ----------
        task : str
            User request.

        Returns
        -------
        list
            List of execution steps.
        """

        task = task.strip()

        task_lower = task.lower()

        if any(word in task_lower for word in ["calculate", "add", "subtract", "multiply", "divide"]):
            return [
                {
                    "description": "Perform calculation",
                    "tool": "calculator",
                    "input": task,
                }
            ]

        if any(word in task_lower for word in ["time", "date", "today", "clock"]):
            return [
                {
                    "description": "Get current date and time",
                    "tool": "datetime",
                    "input": task,
                }
            ]

        if any(word in task_lower for word in ["read", "file", "open"]):
            return [
                {
                    "description": "Read file",
                    "tool": "file_reader",
                    "input": task,
                }
            ]

        return [
            {
                "description": "Echo task",
                "tool": "echo",
                "input": task,
            }
      ]
