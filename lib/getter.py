import pandas as pd
import json
import tweepy


def get_accounts(client, data_frame, sign):

    user_ids = []

    accounts = data_frame[sign].tolist()

    for account in accounts:
        user = client.get_user(username=account)
        user_id = user.data.id
        user_ids.append(user_id)

    return user_ids


def recent_tweets(user_ids, client, sign):

    results = []

    for user_id in user_ids:

        screen_name = client.get_user(id=user_id).data.username
        tweets = tweepy.Paginator(client.get_users_tweets, id=user_id, exclude=['retweets', 'replies'],
                                  max_results=100).flatten(limit=500)

        if tweets is not None:
            for tweet in tweets:
                if len(tweet.text) > 0:
                    obj = {'id': tweet.id, 'text': tweet.text, 'author': screen_name}
                    results.append(obj)
                else:
                    print("Empty!")

    with open('./jsons/horoscope_tweets/'+sign+'_tweets.json', 'w+', encoding='utf-8') as f:
        json.dump(results, f, indent=4)


def main(client, data_frame, sign):
    recent_tweets(get_accounts(client, data_frame, sign), client, sign)
