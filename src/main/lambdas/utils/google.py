import json
import os
import random
import requests
from src.main.lambdas.utils.logs import logger

def search_image(google_secrets,query):
    params = {}
    params['key'] = google_secrets['API_KEY']
    params['cx'] = google_secrets['CX']
    params['q'] = query
    params['searchType'] = 'image'
    params['safe'] = 'active'
    params['start'] = random.randrange(1, 100)
    params['num'] = 1

    response = requests.get(url=os.environ['SEARCH_API'], params=params)

    resp_json = json.loads(response.text)

    link = resp_json['items'][0]['link']

    return link