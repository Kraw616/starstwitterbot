"""
Author: Jacob Krawitz, Jordan Wells, Alek Demaio
Date: 5/9/22
Muhlenberg College 2022, Computer Science CUE

Description:

In this file, tweet data is collected from horoscope accounts located in a .csv file.

"""

# import statements
import pandas as pd
import json
import tweepy


'''
Method: get_accounts()

Description: 

In this method, the user id is taken from the data frame of a given sign.

@params client, data frame, and sign
@returns user ids

'''


def get_accounts(client, data_frame, sign):

    user_ids = []

    accounts = data_frame[sign].tolist()

    # get user information from data frame 
    for account in accounts:
        user = client.get_user(username=account)
        user_id = user.data.id
        user_ids.append(user_id)

    return user_ids


'''
Method: recent_tweets()

Description: 

In this method, tweets are collected from the user ids. 

@params user ids, client, and sign
@returns horoscope tweets .json file

'''


def recent_tweets(user_ids, client, sign):

    results = []

    for user_id in user_ids:

        # get user tweets from user id
        screen_name = client.get_user(id=user_id).data.username
        tweets = tweepy.Paginator(client.get_users_tweets, id=user_id, exclude=['retweets', 'replies'],
                                  max_results=100).flatten(limit=500)

        # if tweets exist, append them to file
        if tweets is not None:
            for tweet in tweets:
                if len(tweet.text) > 0:
                    obj = {'id': tweet.id, 'text': tweet.text, 'author': screen_name}
                    results.append(obj)
                else:
                    print("Empty!")

    # write new tweet .json file
    with open('./jsons/horoscope_tweets/'+sign+'_tweets.json', 'w+', encoding='utf-8') as f:
        json.dump(results, f, indent=4)


'''
Method: main()

Description: 

@params 
@returns 

'''


def main(client, data_frame, sign):
    recent_tweets(get_accounts(client, data_frame, sign), client, sign)
