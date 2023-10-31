import logging
import openai
import os
import azure.functions as func

openai.api_key = os.environ["OPENAI_API_KEY"]

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    req_body = req.get_json()
    dalle_response = getImage(req_body)
    return func.HttpResponse(dalle_response, status_code=200)

def getImage(payload):
    response = openai.Image.create(
        prompt=payload["prompt"],
        n=payload["num"],
        size=payload["size"]
    )
    return response['data'][0]['url']