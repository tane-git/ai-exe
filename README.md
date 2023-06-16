# AI-Executor

## Initial ChatGPT prompt:
I want to create a command line app called ai-executor, that users execute with a string argument called prompt.

This prompt will be a high level desire, like "Create a NodeJS app that prints hello world". 

And this app will then prompt the chatGPT api for terminal commands that it (the app ai-executor) will then automatically execute in the terminal.

The ai-executor will have to prompt the ChatGPT API in such a way that the LLM responds with commands in an expected format. Once the ai-executor executes the command, it will respond to the ChatGPT API with the output from the terminal (if there was any) and then will be expecting the next command from ChatGPT.

The base prompt could look something like this:

```
"You are currently being used within a CLI app called ai-executor,  that allows users to express a high-level desire and have this desire met through the synergy of ai-executor and you, chatgpt. 

The user will prompt ai-executor with a high level desire, and then ai-executor will work with chatgpt to make this happen through the user's terminal.

The users high level desire is: ${desire}

Please respond with your first terminal command to begin working towards this desire.

Then I will respond with the output from the terminal or if there isn't any just 'null'.

Please send commands one at a time and treat my replies as the output from the terminal from running your previous command.

Try to stay 'open-minded' and try everything to fulfil the users high level desire. It won't be easy, they may have run ai-executor in the wrong directory, or while on the wrong branch. 

You have the entire tooling of their terminal at your disposal. For example, figure out where you are (pwd), see where you are (ls), check git information, even make commits, mkdir's etc etc.

Also remember, we want to achieve the user's desire without them having to do much, so for example, to make files and add code, we have to do this through terminal commands that will achieve this. We don't want to ask the user to open a text-editor and copy and paste code as we can do this directly."
```

Before jumping into the implementation of this project feel free to ask for more information, or give me feedback on what I have so far.

Lets work together to make this!


## ChatGPT response:

This is an ambitious and fascinating project! Building a command line interface (CLI) tool that translates high level tasks into terminal commands using an AI is indeed challenging. It's very much the next level of development automation, and quite exciting. Your base prompt to guide the AI is well thought out.

However, we will need to clarify a few points and ensure that some important factors are taken into consideration:

1. **Security and trust issues**: The user should trust the ai-executor to execute terminal commands on their behalf. Executing terminal commands without the user's explicit consent could potentially damage their system. There should be safeguards in place to prevent potential misuse or malicious commands being executed, like `rm -rf /`.

2. **Limitations of AI understanding and context**: The ChatGPT model, as of the last training cut-off in September 2021, does not have a personal memory or context. It's stateless, meaning it doesn't know what it said previously beyond a certain number of tokens (roughly around 2048 for GPT-4). Keeping track of the state between commands could be a challenge.

3. **Error handling**: When an error occurs while executing a command, the system should be able to understand the error message and decide the next appropriate step, which might be quite complex.

4. **Output parsing and understanding**: When a command is executed, the output should be parsed and understood correctly to feed the right response back into ChatGPT.

5. **Limited knowledge about user's system**: ChatGPT does not know about the user's system details (operating system, installed software, etc.). Hence, it might suggest commands which are not applicable or valid.

6. **Code generation**: While creating files and adding code via terminal commands is doable, it can become quite complex if the codebase grows.

Despite these challenges, it's still a very exciting project. Here's a broad outline of how you might implement it:

1. **Create the CLI Application** (using Node.js, Python or any other language of your choice).

2. **Implement the ChatGPT API Integration**. You'll need to make a POST request to the OpenAI API endpoint and handle the response.

3. **Setup a Command Execution Environment**. You'll need a safe way to execute commands and capture the output/error messages. This can be achieved through subprocess or shell scripting libraries in most programming languages.

4. **Command Parsing and Execution**. When you receive a response from the ChatGPT API, parse it to extract the command, execute it, and capture the output.

5. **Output Feedback Loop**. Feed the command output back into the ChatGPT API to guide the next steps. Remember to handle errors appropriately.

6. **User Interaction**. Keep the user informed about what the ai-executor is doing, and perhaps have a mechanism for them to approve or deny certain actions.

7. **Test and Iterate**. Start with a very limited set of tasks, then gradually expand based on how well the system handles them.

Remember, building such a tool is a significant undertaking that will require careful thought and rigorous testing. But with persistence and attention to detail, it could become an exciting new way of automating development tasks! Good luck!