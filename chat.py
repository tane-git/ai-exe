import os
import openai
from dotenv import load_dotenv


def send_message_to_openai(message):
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ],
    )

    response = completion.choices[0].message["content"]

    print("Reponse", response)

    return response
