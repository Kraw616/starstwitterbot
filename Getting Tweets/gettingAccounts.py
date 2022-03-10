

import tweepy
from config import *

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=API_KEY,
                       consumer_secret=API_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_SECRET)


def searchForAccounts():
    seen = set()

    query = " -is:retweet -has:images -has:links -has:mentions lang:en"

    query = "(astrology OR zodiac OR horoscope) (cancer OR taurus OR capricorn OR sagittarius OR libra OR virgo OR leo OR pisces OR aquarius OR aries OR gemini) -has:media -is:retweet lang:en"

    tweets = client.search_recent_tweets(query=query, max_results=10)

    tweet_data = tweets.data

    results = []

    if tweet_data is not None and len(tweet_data) > 0:
        for tweet in tweet_data:
            tweetA = client.get_tweet(tweet.id, expansions='author_id')
            author = tweetA.data.author_id

            if author in seen:
                continue

            numLikes = 0

            for user in client.get_liking_users(tweet.id, user_fields=['username', 'id']):
                print(str(tweet.id) + ":\n")
                print(user.data['result_count'])
                numLikes += user['result_count']

            if numLikes >= 5:
                print(author)
                print(tweet.id)
                obj = {'id': tweet.id, 'text': tweet.text, 'author': author}
                results.append(obj)
                seen.add(author)
            else:
                seen.add(author)
                continue

    else:
        print("Empty!")

    with open("found_accounts.txt", 'a+') as filehandler:
        for tweet in results:
            filehandler.write(str(tweet['id']) + "\n" + tweet['text'] + "\n" + tweet['author'] + "\n\n")
            # print(tweet)
            # print()


def main():

    searchForAccounts()


main()
