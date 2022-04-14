import tweepy
from lib import gemini
from lib import libra

import pandas as pd

import json_practice

from config import *


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=API_KEY,
                       consumer_secret=API_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_SECRET,
                       wait_on_rate_limit=True)

df = pd.read_csv('example_data/libraPosts_test.csv', dtype=str)
df = df.dropna()
print(df)


def main():

    new_df = pd.DataFrame(columns=['ID', 'USER_NAME'], dtype=object)

    for ide in df['ID']:

        print(ide)

        liked_user = client.get_liking_users(ide)
        liked_user = liked_user.data

        if liked_user:
            for user in liked_user:
                new_df = new_df.append({'ID': str(user['id']), 'USER_NAME': str(user['name'])}, ignore_index=True)

    print(new_df)
    new_df.to_csv('liked_users.csv', index=False)


main()
