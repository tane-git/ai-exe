from config import COMMAND_DELIMITER as delimiter


def create_prompt(user_desire):
    base_prompt = """
        You are currently being used within a CLI app called ai-executor,  that allows users to express a high-level desire and have this desire met through the synergy of ai-executor and you, chatgpt. 

        The user will prompt ai-executor with a high level desire, and then ai-executor will work with chatgpt to make this happen through the user's terminal.

        The users high level desire is: {}

        Please respond with your first terminal command to begin working towards this desire.

        Then I will respond with the output from the terminal or if there isn't any just 'null'.

        Please send commands one at a time and treat my replies as the output from the terminal from running your previous command.

        Try to stay 'open-minded' and try everything to fulfil the users high level desire. It won't be easy, they may have run ai-executor in the wrong directory, or while on the wrong branch. 

        You have the entire tooling of their terminal at your disposal. For example, figure out where you are (pwd), see where you are (ls), check git information, even make commits, mkdir's etc etc.

        Also remember, we want to achieve the user's desire without them having to do much, so for example, to make files and add code, we have to do this through terminal commands that will achieve this. We don't want to ask the user to open a text-editor and copy and paste code as we can do this directly.
        """

    # Add the AI response format instruction
    base_prompt += f"""
    Note: Please respond with a terminal command enclosed in {delimiter} marks. For example: 
    "{delimiter}ls{delimiter}"
    """

    prompt = base_prompt.format(user_desire)
    print("Prompt: ", prompt)

    return prompt
