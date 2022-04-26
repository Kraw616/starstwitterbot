import json

unique_users = set()

with open('./jsons/libra_tweets.json') as f:

    f_data = json.load(f)

    print(len(f_data))


with open('./jsons/libra_liked_users.json') as f2:

    f_data2 = json.load(f2)

    print(len(f_data2))


