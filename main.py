from modules.argParser import parse_arguments
from modules.template import create_prompt
from chat import send_message_to_openai
from modules.executor import execute_command
from modules.security import is_command_approved
from modules.extractor import extract_command


def prompting_loop(prompt, depth=0):
    depth = depth + 1

    response = send_message_to_openai(prompt)

    command = extract_command(response)

    if is_command_approved(command):
        stdout, stderr = execute_command(command)

        # output is treated as a response from the user
        if depth < 5:
            prompting_loop(stdout, depth)
        else:
            return

        if stderr:
            print(f"Command errors: {stderr}")
    else:
        print(f"Command {response} is not approved for execution.")


if __name__ == "__main__":
    user_desire = parse_arguments()

    prompt = create_prompt(user_desire)

    prompting_loop(prompt)
