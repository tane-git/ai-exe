from argparser import parse_arguments
from chat import send_message_to_openai
from executor import execute_command
from security import is_command_approved

if __name__ == "__main__":
    user_desire = parse_arguments()
    command = send_message_to_openai(user_desire)
    
    if is_command_approved(command):
        stdout, stderr = execute_command(command)
        print(f"Command output: {stdout}")
        if stderr:
            print(f"Command errors: {stderr}")
    else:
        print(f"Command {command} is not approved for execution.")

