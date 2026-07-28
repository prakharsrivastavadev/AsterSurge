"""
AsterSurge Planner

Version: 0.3.0
"""


class Planner:
    """
    Rule-based planner that converts a task
    into executable steps.
    """

    def create_plan(self, task: str):
        """
        Create an execution plan.
        """

        task_lower = task.lower()

        plan = []

        if any(
            word in task_lower
            for word in (
                "calculate",
                "math",
                "add",
                "subtract",
                "multiply",
                "divide",
            )
        ):
            plan.append(
                {
                    "tool": "calculator",
                    "description": "Perform calculation",
                    "action": task,
                }
            )

        elif any(
            word in task_lower
            for word in (
                "date",
                "time",
                "today",
                "clock",
            )
        ):
            plan.append(
                {
                    "tool": "datetime",
                    "description": "Get current date and time",
                    "action": None,
                }
            )

        elif any(
            word in task_lower
            for word in (
                "read",
                "open",
                "file",
            )
        ):
            plan.append(
                {
                    "tool": "file_reader",
                    "description": "Read file",
                    "action": task,
                }
            )

        else:
            plan.append(
                {
                    "tool": "llm",
                    "description": "Generate response using configured LLM",
                    "action": task,
                }
            )

        return plan

    def validate(self, plan):
        """
        Validate an execution plan.
        """

        if not isinstance(plan, list):
            raise TypeError(
                "Plan must be a list."
            )

        required = {
            "tool",
            "description",
            "action",
        }

        for step in plan:

            if not required.issubset(step):
                raise ValueError(
                    "Invalid execution step."
                )

        return True

    def explain(self, plan):
        """
        Return readable descriptions.
        """

        return [
            step["description"]
            for step in plan
        ]
