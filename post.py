import json, requests


REPOSITORY_UUID = '82b6aca7-2c78-45ce-aa0f-0828e2a9def5'
LANGUAGE = 'pt_br'
AUTH_TOKEN = 'Token 5ef90351e1b8bb19761e98e03773f0d20f3f94de'

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