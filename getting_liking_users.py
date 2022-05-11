"""


Author: Jacob Krawitz, Jordan Wells, Alek Demaio

Date: 5/9/22

Muhlenberg College 2022, Computer Science CUE

Description: 

In this file, users which like given horoscope tweets are recorded and added to a .json file. 


"""

# import statements
import tweepy
from lib import getter
import pandas as pd
import json

# import twitter access credentials
from config import *

# employ twitter access cridentials
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=API_KEY,
                       consumer_secret=API_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_SECRET,
                       wait_on_rate_limit=True)

# assign a zodiac sign
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

# open and load horoscope tweet .json file for given sign
with open('./jsons/horoscope_tweets/'+sign+'_tweets.json') as file:
    sign_tweets = json.load(file)

    
'''


Method: main()

Description: 

@params 
@returns 


'''


def main():

    # create a list for results
    results = []
    
    # create a set for users in file
    known = set()
    
    # set counter to 0
    counter = 0

    # get tweet id for each tweet
    for tweets in sign_tweets:
        tweet_id = tweets['id']

        # get up to 5000 users who liked given horoscope tweets
        liked_users = tweepy.Paginator(client.get_liking_users, id=tweet_id).flatten(limit=5000)

        # create dictionary for user information of liked users
        if liked_users:
            for user in liked_users:
                obj = {'id': user['id'], 'user_name': user['name'], 'liked_tweet': tweet_id}

                # check if the user id is a duplicate
                if user['id'] in known:
                    continue
                    
                # append to file if user is not seen in file already
                else:
                    results.append(obj)
                    known.add(user['id'])

        # write new liked users .json file
        with open('./jsons/liked_users/'+sign+'_liked_users.json', 'w+', encoding='utf-8') as liked:
            json.dump(results, liked, indent=4)

        with open('./jsons/liked_users/'+sign+'_liked_users.json', encoding='utf-8') as f:
            f_data = json.load(f)

            # limit the number of users to 5000
            if len(f_data) >= 5000:
                return

# call the main method
main()
