"""
AsterSurge CLI

Command Line Interface

Version: 0.1
"""

import argparse

from .agent import Agent
from .config import Config


def main():
    parser = argparse.ArgumentParser(
        prog="astersurge",
        description="AsterSurge AI Infrastructure CLI",
    )

    parser.add_argument(
        "task",
        nargs="?",
        help="Task for the agent",
    )

    parser.add_argument(
        "--history",
        action="store_true",
        help="Show conversation history",
    )

    parser.add_argument(
        "--config",
        action="store_true",
        help="Show configuration",
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Show version",
    )

    args = parser.parse_args()

    if args.version:
        print(f"{Config.APP_NAME} {Config.VERSION}")
        return

    if args.config:
        Config.print_config()
        return

    agent = Agent()

    if args.history:
        history = agent.history()

        if not history:
            print("No conversation history.")
            return

        for message in history:
            print(
                f"[{message['role']}] {message['content']}"
            )
        return

    if args.task:
        result = agent.run(args.task)

        print("\nTask:")
        print(result["task"])

        print("\nExecution Plan:")
        for step in result["plan"]:
            print(f"- {step['description']}")

        print("\nResults:")
        for item in result["results"]:
            print(f"- {item['step']}: {item['output']}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
