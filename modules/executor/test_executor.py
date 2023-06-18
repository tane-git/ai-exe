import subprocess
from modules.executor import execute_command


def test_execute_command():
    command = "echo Hello, World!"
    output, error = execute_command(command)
    assert output == "Hello, World!"
    assert error == ""


def test_execute_command_no_output():
    command = "cd .."
    output, error = execute_command(command)
    assert output == ""
    assert error == ""


def test_execute_command_invalid():
    command = "nonexistentcommand"
    output, error = execute_command(command)
    assert output == ""
    assert "not found" in error
