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
    known = set()

    for tweets in libra_tweets:
        tweet_id = tweets['id']

        liked_users = tweepy.Paginator(client.get_liking_users, id=tweet_id).flatten(limit=5000)

        if liked_users:
            for user in liked_users:
                obj = {'id': user['id'], 'user_name': user['name'], 'liked_tweet': tweet_id}

                if user['id'] in known:
                    continue
                else:
                    results.append(obj)
                    known.add(user['id'])

        with open('./jsons/libra_liked_users.json', 'w+', encoding='utf-8') as liked:
            json.dump(results, liked, indent=4)

        with open('./jsons/libra_liked_users.json', encoding='utf-8') as f:
            f_data = json.load(f)

            if len(f_data) >= 5000:
                return



main()
