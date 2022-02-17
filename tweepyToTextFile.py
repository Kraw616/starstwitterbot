import tweepy
from config import *

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)


client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key = API_KEY,
                       consumer_secret = API_SECRET,
                       access_token = ACCESS_TOKEN,
                       access_token_secret = ACCESS_SECRET)

file_name = 'tweets.txt'


query = "astrology -is:retweet lang:en"
tweets = client.search_recent_tweets(query=query, max_results=10)

tweet_data = tweets.data

results = []

if not tweet_data is None and len(tweet_data) > 0:
    for tweet in tweet_data:
        obj = {}
        obj['id'] = tweet.id
        obj['text'] = tweet.text
        results.append(obj)
else:
    print("Empty!")

with open(file_name, 'a+') as filehandler: 
    for tweet in results:
        filehandler.write(str(tweet['id']) + ":" + tweet['text'] + "\n\n")
        #print(tweet)
        #print()
