"""


Author: Jacob Krawitz, Jordan Wells, Alek Demaio
Date: 5/10/22
Muhlenberg College 2022, Computer Science CUE

Description: In this file, the timeline tweets of the users which liked the given horoscope 
content are collected. 


"""


# import statements
import os.path
import tweepy
from lib import getter
import json
import pandas as pd

# import twitter access credentials
from config import *

# CREATE TWEEPY OBJECT
# employ twitter access credentials

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=API_KEY,
                       consumer_secret=API_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_SECRET,
                       wait_on_rate_limit=True)

# assign a zodiac sign
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

In this method, timeline tweets for users which liked given horoscope content
are collected and added to a .json file in a directory for each user. Up to 50 tweets from the user's timeline is collected,
from 1,000 different users.


'''


def main():
    user_num_id = 0

    # open and load liked users .json file
    with open('./jsons/liked_users/'+sign+'_liked_users.json') as f:

        f_data = json.load(f)

        for user in f_data:

            # create list for results
            results = []

            # set tweet number to 1
            tweet_number = 1

            # set the user name from the user dictionary
            user_name = user['user_name']
            
            # set the user id from the user dictionary
            user_id = user['id']


             # collect up to 50 of the users' timeline tweets excluding retweets
            tweets = tweepy.Paginator(client.get_users_tweets, id=user_id, exclude=['retweets', 'replies'],
                                      tweet_fields=['lang'], max_results=50).flatten(limit=50)

            if tweets is not None:
                for tweet in tweets:
                  
                    # make sure tweet exsists
                    if len(tweet.text) > 0:
                      
                        # make sure tweet is in english
                        if tweet.lang == 'en':
                            
                            # create dictionary for user information and tweet data
                            obj = {'user_num_id': user_num_id, 'user_id': user_id, 'author': user_name, 'tweet_num': tweet_number, 'tweet_id': tweet.id,
                                   'lang': tweet.lang, 'text': tweet.text}
                            
                            # append user information and tweet to file
                            results.append(obj)
                            
                            # count the number of tweets
                            tweet_number += 1
                    else:
                        print("Empty!")

            # make directory for each user
            if not os.path.exists('./jsons/users_timeline_tweets/'+sign+'/'+str(user_num_id)):
                os.makedirs('./jsons/users_timeline_tweets/'+sign+'/'+str(user_num_id))

            # write tweet data and information into a .JSON file
            with open('./jsons/users_timeline_tweets/'+sign+'/'+str(user_num_id)+'/'+str(user_num_id)+'.json', 'w+') as out:
                json.dump(results, out, indent=4)

            # limit set to 1000 users
            if user_num_id == 1000: 
                return

            # count the number of user ids
            user_num_id += 1

# call the main method
main()
