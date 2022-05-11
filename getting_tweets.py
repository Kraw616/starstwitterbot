"""
Author: Jacob Krawitz, Jordan Wells, Alek Demaio
Date: 5/9/22
Muhlenberg College 2022, Computer Science CUE

Description:

In this file, the main function of the getter.py file is called to collect tweet data. 

"""


# import statements
import tweepy
from lib import getter
import pandas as pd

# import twitter access credentials 
from config import *

# access twitter access credentials 
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=API_KEY,
                       consumer_secret=API_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_SECRET)

# read in csv file
df = pd.read_csv('accounts.csv')

# assing the zodiac sign
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

    # call the main method from the getter file
    getter.main(client, df, sign)

# call the main method
main()
