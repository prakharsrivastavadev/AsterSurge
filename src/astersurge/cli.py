"""
AsterSurge CLI

Version: 0.3.0
"""

import argparse

from .agent import Agent
from .config import Config
from .factory import ProviderFactory


def main():
    parser = argparse.ArgumentParser(
        prog="astersurge",
        description="AsterSurge AI Framework",
    )

    subparsers = parser.add_subparsers(
        dest="command",
    )

    chat_parser = subparsers.add_parser(
        "chat",
        help="Chat with AsterSurge",
    )

    chat_parser.add_argument(
        "prompt",
        nargs="+",
        help="Prompt to send",
    )

    subparsers.add_parser(
        "providers",
        help="List available providers",
    )

    subparsers.add_parser(
        "config",
        help="Show configuration",
    )

    subparsers.add_parser(
        "version",
        help="Show version",
    )

    args = parser.parse_args()

    if args.command == "version":
        print(
            f"{Config.APP_NAME} {Config.VERSION}"
        )
        return

    if args.command == "config":
        for key, value in Config.as_dict().items():
            print(f"{key}: {value}")
        return

    if args.command == "providers":
        print(
            "\n".join(
                ProviderFactory.available()
            )
        )
        return

    if args.command == "chat":
        prompt = " ".join(args.prompt)

        agent = Agent(
            provider=Config.PROVIDER,
            model=Config.MODEL,
        )

        response = agent.chat(prompt)

        print(response)
        return

    parser.print_help()


if __name__ == "__main__":
    main()
