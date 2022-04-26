<<<<<<< Updated upstream
import pandas as pd
=======
import json
import tweepy
>>>>>>> Stashed changes


def get_libra_accounts(client, data_frame):

    user_ids = []

    accounts = data_frame['Libra'].tolist()

    for account in accounts:
        user = client.get_user(username=account)
        user_id = user.data.id
        user_ids.append(user_id)

    return user_ids


def libra_recent_tweets(user_ids, client):

    df = pd.DataFrame(columns=['ID', 'TEXT', 'AUTHOR'])

<<<<<<< Updated upstream
    file_name = "libraPosts.txt"

    for user_id in user_ids:

        screen_name = client.get_user(id=user_id).data.username

        tweets = client.get_users_tweets(id=user_id, exclude=['retweets', 'replies'], max_results=10)
        tweets_data = tweets.data

        results = []

        if tweets_data is not None and len(tweets_data) > 0:
            for tweet in tweets_data:
                obj = {'id': tweet.id, 'text': tweet.text, 'author': screen_name}
                results.append(obj)
        else:
            print("Empty!")

        with open(file_name, 'a+') as filehandler:
            filehandler.write(screen_name + "\n" + "-" * 101 + "\n\n")
            for tweet in results:
                filehandler.write(str(tweet['id']) + ":" + tweet['text']+"\n\n")

                df = df.append({'ID': tweet['id'], 'TEXT': tweet['text'], 'AUTHOR': tweet['author']}, ignore_index=True)
                # print(tweet)
                # print()
        filehandler.close()

        df.to_csv('libraPosts.csv', index=False, float_format='{:f}')
=======
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

    with open('./jsons/libra_tweets.json', 'w+', encoding='utf-8') as f:
        json.dump(results, f, indent=4)
>>>>>>> Stashed changes


def main(client, data_frame):
    libra_recent_tweets(get_libra_accounts(client, data_frame), client)
