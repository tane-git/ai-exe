from modules.template.template import create_prompt
from config import COMMAND_DELIMITER as delimiter


def test_create_prompt():
    user_desire = "I want to print 'Hello, world!'"
    prompt = create_prompt(user_desire)

    assert user_desire in prompt, "The prompt should include the user's desire."

    assert (
        delimiter in prompt
    ), f"The prompt should include the command delimiter '{delimiter}'."
