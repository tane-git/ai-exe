import os
import openai
from dotenv import load_dotenv
from modules.template import get_system_content

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [
    {"role": "system", "content": get_system_content()},
]


def send(message):
    messages.append({"role": "user", "content": message})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    response = completion.choices[0].message["content"]

    messages.append({"role": "system", "content": response})

    return response
