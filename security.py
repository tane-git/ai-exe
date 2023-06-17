# security.py

approved_commands = ["ls", "pwd", "cd"]

def is_command_approved(command):
    # Extract the first word (actual command) from the command string
    command_name = command.split()[0]
    
    if command_name in approved_commands:
        return True
    else:
        return False

