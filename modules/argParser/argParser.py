import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="AI Executor that runs high-level commands."
    )

    parser.add_argument("desire", type=str, help="The high-level desire to be executed")
    parser.add_argument(
        "-p", "--pause", action="store_true", help="Pause before each command"
    )

    args = parser.parse_args()

    return args
