import json


def get_gemini_accounts(client, data_frame):

    user_ids = []

    accounts = data_frame['Gemini'].tolist()

    for account in accounts:
        user = client.get_user(username=account)
        user_id = user.data.id
        user_ids.append(user_id)

    return user_ids


def gemini_recent_tweets(user_ids, client):

    for user_id in user_ids:

        screen_name = client.get_user(id=user_id).data.username

        tweets = client.get_users_tweets(id=user_id, exclude=['retweets', 'replies'], max_results=20)
        tweets_data = tweets.data

        results = []

        if tweets_data is not None and len(tweets_data) > 0:
            for tweet in tweets_data:
                obj = {'id': tweet.id, 'text': tweet.text, 'author': screen_name}
                results.append(obj)
        else:
            print("Empty!")

    with open('./jsons/gemini_tweets.json') as r:
        data = json.load(r)

    for tweet in results:
        data.append(tweet)

    with open('./jsons/gemini_tweets.json', 'w+') as f:
        json.dump(data, f, indent=4)


def main(client, data_frame):
    gemini_recent_tweets(get_gemini_accounts(client, data_frame), client)
