import json
from nrclex import NRCLex

with open('preProsLibra.json', 'r') as f:
    data = json.load(f)

for tweets in data:
    text_object = NRCLex('preProsLibra.json')
    text_joined = NRCLex(' '.join(tweets['text']))
    print('\n', 'User ID (', tweets['id'], ') :', tweets['text'],
          '\n', text_joined.raw_emotion_scores,
          '\n', text_joined.top_emotions, '\n')