import tweepy
from lib import getter

import pandas as pd

from config import *


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=API_KEY,
                       consumer_secret=API_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_SECRET)

df = pd.read_csv('accounts.csv')

sign = 'aquarius'

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


def main():

    getter.main(client, df, sign)
    # libra.main(client, df)


main()
