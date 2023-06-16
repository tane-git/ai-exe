import argparse
from chat import send_message_to_openai


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="AI Executor that runs high-level commands."
    )
    parser.add_argument("desire", type=str, help="The high-level desire to be executed")

    args = parser.parse_args()
    return args.desire


if __name__ == "__main__":
    user_desire = parse_arguments()
    response = send_message_to_openai(user_desire)
    print(f"OpenAI's response: {response}")
