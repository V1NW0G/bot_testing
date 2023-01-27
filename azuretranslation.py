import requests, uuid, json
import os
from dotenv import load_dotenv

def engtochi(input):
    load_dotenv()

    key = os.getenv('AZURE_KEY')
    endpoint = os.getenv('ENDPOINT')
    location = os.getenv('LOCATION')

    path = '/translate'
    constructed_url = endpoint + path

    translate_text = input

    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': ['yue']
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{'text': translate_text,}]
    print(body)
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    output = json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
    # print(output)
    start = ' "text": "'
    end = '",'

    translated_text = output[output.find(start) + len(start):output.rfind(end)]
    return translated_text

def chitoeng(input):
    load_dotenv()

    key = os.getenv('AZURE_KEY')
    endpoint = os.getenv('ENDPOINT')
    location = os.getenv('LOCATION')

    path = '/translate'
    constructed_url = endpoint + path

    translate_text = input

    params = {
        'api-version': '3.0',
        'from': 'yue',
        'to': ['en']
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{'text': translate_text}]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    output = json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
    # print(output)
    start = ' "text": "'
    end = '",'

    translated_text = output[output.find(start) + len(start):output.rfind(end)]
    return translated_text

