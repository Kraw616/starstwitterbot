import pandas as pd


def get_gemini_accounts(client, data_frame):

    user_ids = []

    accounts = data_frame['Gemini'].tolist()

    for account in accounts:
        user = client.get_user(username=account)
        user_id = user.data.id
        user_ids.append(user_id)

    return user_ids


def gemini_recent_tweets(user_ids, client):

    df = pd.DataFrame(columns=['ID', 'TEXT', 'AUTHOR'])

    file_name = "geminiPosts.txt"

    for user_id in user_ids:
        '''query = "from:" + account + " -is:retweet -has:images -has:links -has:mentions lang:en"

        tweets = client.search_recent_tweets(query=query, max_results=50)'''

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
                #print(tweet)
                #print()
        filehandler.close()

        df.to_csv('geminiPosts.csv', index=False, float_format='{:f}')


def main(client, data_frame):
    gemini_recent_tweets(get_gemini_accounts(client, data_frame), client)
