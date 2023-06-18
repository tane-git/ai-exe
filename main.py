from modules.argParser import parse_arguments
from modules.template.template import create_prompt
from modules.chat import send
from modules.executor import execute_command
from modules.security import is_command_approved
from modules.extractor import extract_command
from modules.pause import maybePause
from config import COMMAND_DELIMITER as delimiter

args = None


def prompting_loop(message, depth=0):
    depth = depth + 1

    if depth > 1:
        print("message: ", message)

    response = send(message)
    print("response: ", response)

    command = extract_command(response)

    if command == None:
        message = f"Message from AI-exector: Your message did not include a {delimiter}command{delimiter}. Please remember that I only process commands. Thank You!"
        prompting_loop(message, depth)

    # if is_command_approved(command):
    if True:
        maybePause(command, args.pause)

        stdout, stderr = execute_command(command)

        if stderr == "":
            nextMessage = f"Message from AI-exector: Your command ({command}) was executed successfully. Here is the output: '{stdout}'"

        # output is treated as a response from the user
        if depth < 10:
            prompting_loop(nextMessage, depth)
        else:
            print("depth met")
            return

        if stderr:
            print(f"Command errors: {stderr}")
    else:
        print(f"Command {response} is not approved for execution.")


if __name__ == "__main__":
    args = parse_arguments()
    user_desire = args.desire

    prompt = create_prompt(user_desire)

    prompting_loop(prompt)
