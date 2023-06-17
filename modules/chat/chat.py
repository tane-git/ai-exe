import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

conversation = []


def send_message_to_openai(message):
    conversation.append({"role": "user", "content": message})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # messages=[
        #     {"role": "system", "content": "You are a helpful assistant."},
        #     {"role": "user", "content": message},
        # ],
        messages=conversation,
    )

    response = completion.choices[0].message["content"]

    conversation.append({"role": "system", "content": response})

    print("Reponse", response)

    return response
