from config import COMMAND_DELIMITER as delimiter
import re


def extract_command(response):
    command_pattern = rf"{delimiter}(.*?){delimiter}"
    match = re.search(command_pattern, response)

    command = match.group(1) if match else None

    print(f"command: {delimiter}{command}{delimiter}")

    return command
