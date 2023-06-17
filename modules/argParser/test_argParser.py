import sys
import pytest
import io
import argparse
from unittest import mock

from modules.argParser import parse_arguments


def test_parse_arguments():
    test_arg = "Create a Python app"

    with mock.patch(
        "argparse.ArgumentParser.parse_args",
        return_value=argparse.Namespace(desire=test_arg),
    ):
        assert parse_arguments() == test_arg


def test_unexpected_argument():
    test_args = ["main.py", "Create a Python app", "unexpected_arg"]

    with mock.patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            parse_arguments()

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2


def test_help_message():
    test_args = ["main.py", "-h"]

    with mock.patch.object(sys, "argv", test_args), mock.patch(
        "sys.stdout", new_callable=io.StringIO
    ) as mock_stdout:
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            parse_arguments()

    help_message = mock_stdout.getvalue()

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

    assert "AI Executor that runs high-level commands." in help_message
    assert "The high-level desire to be executed" in help_message
