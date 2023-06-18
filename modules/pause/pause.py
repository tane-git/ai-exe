from emoji import emojize
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)


def maybePause(command, pause):
    print(emojize("command: "), Fore.RED + command, end="")
    if pause:
        print(emojize(" :pause_button: "), end="")
        print("(press 'enter' to continue or type 'off' to disable pause mode)")
        user_input = input()

        if user_input.strip().lower() == "off":
            pause = False
    else:
        print()
