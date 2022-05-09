"""
Author: Jacob Krawitz,
Date: 5/9/22
Muhlenberg College 2022, Computer Science CUE

Description:

"""

import os.path

import tweepy
from lib import getter
import json

import pandas as pd

from config import *


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=API_KEY,
                       consumer_secret=API_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_SECRET,
                       wait_on_rate_limit=True)

sign = 'cancer'

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


'''
Method: main()

Description: 

@params 
@returns 

'''


def main():
    user_num_id = 0

    with open('./jsons/liked_users/'+sign+'_liked_users.json') as f:

        f_data = json.load(f)

        for user in f_data:

            results = []

            tweet_number = 1

            user_name = user['user_name']
            user_id = user['id']

            tweets = tweepy.Paginator(client.get_users_tweets, id=user_id, exclude=['retweets', 'replies'],
                                      tweet_fields=['lang'], max_results=50).flatten(limit=50)

            if tweets is not None:
                for tweet in tweets:
                    if len(tweet.text) > 0:
                        if tweet.lang == 'en':
                            obj = {'user_num_id': user_num_id, 'user_id': user_id, 'author': user_name, 'tweet_num': tweet_number, 'tweet_id': tweet.id,
                                   'lang': tweet.lang, 'text': tweet.text}
                            results.append(obj)
                            tweet_number += 1
                    else:
                        print("Empty!")

            # Make directory for each user
            if not os.path.exists('./jsons/users_timeline_tweets/'+sign+'/'+str(user_num_id)):
                os.makedirs('./jsons/users_timeline_tweets/'+sign+'/'+str(user_num_id))

            with open('./jsons/users_timeline_tweets/'+sign+'/'+str(user_num_id)+'/'+str(user_num_id)+'.json', 'w+') as out:
                json.dump(results, out, indent=4)

            if user_num_id == 1000: # 5000 users 10 max tweets
                return

            user_num_id += 1


main()
