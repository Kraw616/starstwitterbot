import pandas as pd


def get_gemini_accounts(client):
    user_ids = []

    accounts = []

    f = open("accounts.txt", 'r')

    for line in f:
        if "Gemini:" in line:
            accounts.append(f.readline().strip())
            accounts.append(f.readline().strip())
            accounts.append(f.readline().strip())

    f.close()

    for account in accounts:
        user = client.get_user(username=account)
        user_id = user.data.id
        user_ids.append(user_id)

    return user_ids


def gemini_recent_tweets(user_ids, client):

    file_name = "geminiPosts.txt"

    for user_id in user_ids:
        '''query = "from:" + account + " -is:retweet -has:images -has:links -has:mentions lang:en"

        tweets = client.search_recent_tweets(query=query, max_results=50)'''

        screen_name = client.get_user(id=user_id).data.username

        tweets = client.get_users_tweets(id=user_id, exclude=['retweets', 'replies'], max_results=50)
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
                #print(tweet)
                #print()
        filehandler.close()


def main(client):
    gemini_recent_tweets(get_gemini_accounts(client), client)
