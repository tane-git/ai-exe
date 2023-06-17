import argparse
from chat import send_message_to_openai
from executor import execute_command


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="AI Executor that runs high-level commands."
    )
    parser.add_argument("desire", type=str, help="The high-level desire to be executed")

    args = parser.parse_args()
    return args.desire


if __name__ == "__main__":
    user_desire = parse_arguments()
    command = send_message_to_openai(user_desire)
    print(command)
    test = "ls"
    stdout, stderr = execute_command(test)
    print(f"Command output: {stdout}")
    if stderr:
        print(f"Command errors: {stderr}")
