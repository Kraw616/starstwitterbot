import tweepy
from lib import gemini
from lib import libra

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

df = pd.read_csv('accounts.csv')


def main():

    #gemini.main(client, df)
    libra.main(client, df)


main()
