import json, requests
from settings import *

def categorize_req(url, headers, data):
    request = requests.post(url, headers=headers, data=data)
    json = request.json()
    intent = json.get('intent', {}).get('name')
    acuracia = json.get('intent', {}) .get('confidence')
    acuracia = acuracia*100

    resposta = [intent, acuracia]
    return resposta

def create_test(text, intent):
    url = 'https://api.bothub.it/v2/evaluate/'
    data_req = {
                "repository": REPOSITORY_UUID,
                "text": text,
                "language":LANGUAGE,
                "entities":[],
                "intent": intent
            }
    headers = {
                'Content-Type': 'application/json',
                'Authorization': AUTH_TOKEN,
            }

    print(f'{requests.post(url, data=json.dumps(data_req), headers=headers)}\n')