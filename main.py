from modules.argParser import parse_arguments
from modules.template.template import create_prompt
from modules.chat import send
from modules.executor import execute_command
from modules.security import is_command_approved
from modules.extractor import extract_command

# Styles
from colorama import init, Fore, Back, Style
from emoji import emojize

# Initialize colorama
init(autoreset=True)


args = None


def communicate(command):
    print(emojize("command: "), Fore.RED + command, end="")
    if args.pause:
        print(emojize(" :pause_button: "), end="")
        print("(press 'enter' to continue or type 'off' to disable pause mode)")
        users_input = input()

        if users_input == "off":
            args.pause = False
    else:
        print()


def prompting_loop(message, depth=0):
    depth = depth + 1

    if depth > 1:
        print("message: ", message)

    response = send(message)
    print("response: ", response)

    command = extract_command(response)

    if command == None:
        message = "Message from AI-exector: Your message did not include a command. Please remember that only commands will be processed."
        prompting_loop(message, depth)

    # if is_command_approved(command):
    if True:
        communicate(command)

        stdout, stderr = execute_command(command)

        if stdout == "" and stderr == "":
            stdout = f"Message from AI-exector: Your command ({command}) was executed successfully but did not contain any output. Please continue sending commands."

        # output is treated as a response from the user
        if depth < 10:
            prompting_loop(stdout, depth)
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
