# argparser.py
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='AI Executor that runs high-level commands.')
    parser.add_argument('desire', type=str, help='The high-level desire to be executed')

    args = parser.parse_args()
    return args.desire

