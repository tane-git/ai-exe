from config import COMMAND_DELIMITER
import re


def extract_command(response):
    command_pattern = rf"{COMMAND_DELIMITER}(.*?){COMMAND_DELIMITER}"
    match = re.search(command_pattern, response)

    command =  match.group(1) if match else None

    return command
