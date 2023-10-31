import openai
import os
import webbrowser
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

save_file = "save.txt"

def save_txt(new_url):
    if not os.path.exists(save_file):
        with open(save_file, "w") as file:
            file.write(new_url + "\n")
    else:
        with open(save_file, "a") as file:
            file.write(new_url + "\n")
    print("url saved")
    webbrowser.open(new_url)

def getImage(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']

prompt = "A pretty perfect woman with beautiful eyes and skin by Alan Lee, digital art"
dalle_response = getImage(prompt)
print(dalle_response)
save_txt(dalle_response)