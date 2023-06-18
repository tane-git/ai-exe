from unittest import mock
from modules.chat import send


def test_send_message_to_openai():
    mock_message = mock.MagicMock()
    mock_message.configure_mock(**{"message": {"content": "Mock response"}})

    mock_choices = mock.MagicMock()
    mock_choices.configure_mock(**{"__getitem__.return_value": mock_message})

    mock_response = mock.MagicMock()
    mock_response.configure_mock(**{"choices": mock_choices})

    with mock.patch("openai.ChatCompletion.create", return_value=mock_response):
        response = send("Test message")

    assert response == "Mock response"
