import requests
import random
from keys import oxford
from syllables import count_syllables_word

def get_candidates(string, n=4, model=random.choice(['body', 'title', 'anchor'])):
    print model
    print string
    params = {'words': string, 'model': model, 'maxNumOfCandidatesReturned': n}
    headers = {'Ocp-Apim-Subscription-Key': oxford}
    url = 'https://api.projectoxford.ai/text/weblm/v1.0/generateNextWords'
    r = requests.post(url, params=params, headers=headers)
    if r.status_code == 200:
        return r.json()['candidates']
    else:
        print('error retrieving canidates from oxford')
        print r.json()
        return []

def get_candidates_in_range(string, max_syllables):
    # here each candidate is a list of tuples of (word, syllable_count)
    candidates = []
    r = get_candidates(string, 20)
    # r.sort(key=lambda c: c['probability'])
    random.shuffle(r)
    for candidate in r:
        s = count_syllables_word(candidate['word'])
        if s <= max_syllables:
            candidates.append((candidate['word'], s))
    return candidates
