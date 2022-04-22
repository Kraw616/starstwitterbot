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
        tweet_id = tweets['id']

        liked_users = client.get_liking_users(tweet_id)
        liked_users = liked_users.data

        if liked_users:
            for user in liked_users:
                obj = {'id': user['id'], 'user_name': user['name'], 'liked_tweet': tweet_id}
                results.append(obj)

        with open('./jsons/libra_liked_users.json', 'w+', encoding='utf-8') as liked:
            json.dump(results, liked, indent=4)

        '''with open('./jsons/libra_liked_users.json', encoding='utf-8') as liked:

            file_data = json.load(liked)

            if liked_users:
                for user in liked_users:
                    if user['id'] not in file_data:
                        obj = {'id': user['id'], 'user_name': user['name'], 'liked_tweet': tweet_id}
                        results.append(obj)

            print("SIZE: " + str(len(file_data)))

            file_data.append(results)

            liked.seek(0)

            print("NEW SIZE: " + str(len(file_data)))

            json.dump(file_data, liked, indent=4)'''


main()
