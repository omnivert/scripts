#!/usr/bin/python3

import pprint
import requests
from datetime import datetime
import json

#============ request parameters ===========

GLOBAL_PARAMS = {
    'action': 'query',
    'prop': 'revisions',
    'titles': '',
    'rvprop': 'timestamp|user|comment|size',  
    'rvslots': 'main',
    'formatversion': '2',
    'format': 'json',
    'rvlimit': '500' 
}

#TODO argparse
#TODO logging rather than printing debug messages

# CURRENTLY HARDCODING THINGS JUST TO GET FIRST COMMIT
lang = 'en'
base_url = 'https://{}.wikipedia.org/w/api.php'.format(lang)
article_title = 'Palestine'#'Lim Yo-hwan'
'''
EN_DICT = { 
    'kash_en': 'Kashmir conflict', 
    'article_en': 'Article 370 of the Constitution of India', 
    'insurg_en': 'Insurgency in Jammu and Kashmir' 
}
'''

# MORE HARDCODING
articles = [article_title]

#============ revision history request ===========

S = requests.Session()

for article in articles:
    # point to correct lang-specific article, reset rvcontinue
    GLOBAL_PARAMS['titles'] = article
    if 'rvcontinue' in GLOBAL_PARAMS:
        del GLOBAL_PARAMS['rvcontinue']

    # first request, variable init befor loop
    R = S.get(url=base_url, params=GLOBAL_PARAMS)
    DATA = R.json()
    revisions = DATA['query']['pages'][0]['revisions']
    print(len(revisions))

    # if total > rvlimit, API will chunk it and offer 'continue' param
    # which just needs to be added to the next request
    while True:
        if 'continue' in DATA:
            print(DATA['continue'])
            GLOBAL_PARAMS['rvcontinue'] = DATA['continue']['rvcontinue']
            R = S.get(url=base_url, params=GLOBAL_PARAMS)
            DATA = R.json()
            newrevs = DATA['query']['pages'][0]['revisions']
            print(len(newrevs))
            revisions += newrevs
        else:
            print('==============END==============')
            break

    print('{} total revisions'.format(len(revisions)))
