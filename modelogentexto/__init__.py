import logging
import openai
import os
import azure.functions as func

openai.api_key = os.environ["OPENAI_API_KEY"]

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    req_body = req.get_json()
    gpt_response = ask_chat_gpt(req_body)
    return func.HttpResponse(f"🤖GPT: {gpt_response}", status_code=200)

def ask_chat_gpt(payload):
    response = openai.Completion.create(
        model=payload["model"],
        prompt=payload["prompt"],
        n=1,
        max_tokens=payload["max_tokens"],
        temperature=payload["temperature"]
    )
    return response['choices'][0]['text'].strip()