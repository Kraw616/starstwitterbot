"""
Author: Jacob Krawitz,
Date: 5/9/22
Muhlenberg College 2022, Computer Science CUE

Description:

"""

import tweepy
from lib import getter

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

sign = 'pisces'

'''
'libra'
'gemini'
'aries'
'taurus'
'cancer'
'leo'
'virgo'
'scorpio'
'sagittarius'	
'capricorn'
'aquarius'	
'pisces'
'''

with open('./jsons/horoscope_tweets/'+sign+'_tweets.json') as file:
    sign_tweets = json.load(file)

'''
Method: main()

Description: 

@params 
@returns 

'''


def main():

    results = []
    known = set()
    counter = 0

    for tweets in sign_tweets:
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

        with open('./jsons/liked_users/'+sign+'_liked_users.json', 'w+', encoding='utf-8') as liked:
            json.dump(results, liked, indent=4)

        with open('./jsons/liked_users/'+sign+'_liked_users.json', encoding='utf-8') as f:
            f_data = json.load(f)

            if len(f_data) >= 5000:
                return


main()
