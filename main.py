import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='AI Executor that runs high-level commands.')
    parser.add_argument('desire', type=str, help='The high-level desire to be executed')

    args = parser.parse_args()
    return args.desire

if __name__ == "__main__":
    user_desire = parse_arguments()
    print(f"User's desire: {user_desire}")

