import json

unique_users = set()

with open('./jsons/libra_liked_users.json') as f:

    f_data = json.load(f)

    for user in f_data:
        if user['id'] not in unique_users:
            unique_users.add(user['id'])
        else:
            continue



    print(len(f_data))
    print(len(unique_users))