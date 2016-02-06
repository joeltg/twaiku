import requests
from keys import oxford

def get_candidates(string, model='body'):
    params = {'words': string, 'model': model}
    headers = {'Ocp-Apim-Subscription-Key': oxford}
    url = 'https://api.projectoxford.ai/text/weblm/v1.0/generateNextWords'
    r = requests.post(url, params=params, headers=headers)
    if r.status_code == 200:
        return r.json()['candidates']
    else:
        print('error retrieving canidates from oxford')
        return r.json()

print(get_candidates('yesterday I went to the'))
