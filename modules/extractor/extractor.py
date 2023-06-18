from config import COMMAND_DELIMITER
import re


def extract_command(response, delimiter=COMMAND_DELIMITER):
    escaped_delimiter = re.escape(delimiter)
    command_pattern = f"{escaped_delimiter}(.*?){escaped_delimiter}"
    match = re.search(command_pattern, response)

    command = match.group(1) if match else None

    return command
