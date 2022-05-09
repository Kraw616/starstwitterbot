"""
Author: Jacob Krawitz,
Date: 5/9/22
Muhlenberg College 2022, Computer Science CUE

Description:

"""

# IMPORT STATEMENTS
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

'''
Method: main()

Description: Driver method for the file. Calls the getter.py file to run its main method.

@params None
@returns None

'''


def main():

    getter.main(client, df, sign)
    # libra.main(client, df)


main()
