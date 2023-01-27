import requests, uuid, json
import os
from dotenv import load_dotenv

load_dotenv()

# Add your key and endpoint
key = os.getenv('AZURE_KEY')
endpoint = os.getenv('ENDPOINT')

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = os.getenv('LOCATION')

path = '/translate'
constructed_url = endpoint + path

def engtochi():
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
    body = [{
        'text': 'my exam is poor, i want to die. Please visit https://learn.microsoft.com/zh-tw/azure/cognitive-services/translator/dynamic-dictionary',
}]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    output = json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
    # print(output)
    start = ' "text": "'
    end = '",'

    print(output[output.find(start) + len(start):output.rfind(end)])

def chitoeng():
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
    body = [{
        'text': 'my exam is poor, i want to die. Please visit https://learn.microsoft.com/zh-tw/azure/cognitive-services/translator/dynamic-dictionary'
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    output = json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
    # print(output)
    start = ' "text": "'
    end = '",'

    print(output[output.find(start)+len(start):output.rfind(end)])

engtochi()
chitoeng()