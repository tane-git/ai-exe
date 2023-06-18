from modules.extractor import extract_command
from config import COMMAND_DELIMITER as delimiter


def test_extract_command():
    response = f"Your command should be: {delimiter}ls{delimiter}"
    command = extract_command(response)
    assert command == "ls"


def test_extract_command_no_command():
    response = "There is no command here."
    command = extract_command(response)
    assert command is None


def test_extract_command_multiple_commands():
    response = (
        f"Do this: {delimiter}ls{delimiter}, then do this: {delimiter}pwd{delimiter}"
    )
    command = extract_command(response)
    assert command == "ls"  # Should only return the first command
