import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def ask_chat_gpt(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        n=1,
        max_tokens=100,
        temperature=0.5
    )
    return response['choices'][0]['text'].strip()

prompt = "Necesito un titulo de 5 palabras para una pelicula de ciencia ficcion"
gpt_response = ask_chat_gpt(prompt)
print(f"{gpt_response}")