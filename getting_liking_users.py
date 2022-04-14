import tweepy
from lib import gemini
from lib import libra

import pandas as pd
import json

from config import *


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=API_KEY,
                       consumer_secret=API_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_SECRET,
                       wait_on_rate_limit=True)

with open('./jsons/libra_tweets.json') as file:
    libra_tweets = json.load(file)


def main():

    results = []

    for tweets in libra_tweets:
        user_id = tweets['id']

        liked_user = client.get_liking_users(user_id)
        liked_user = liked_user.data

        if liked_user:
            for user in liked_user:
                obj = {'id': user['id'], 'user_name': user['name']}
                results.append(obj)

    with open('./jsons/libra_liked_users.json', 'w+') as f:
        json.dump(results, f, indent=4)


main()
