import json

practice_json = [
    {
        'id': 555,
        'user_name': "bob",
        'liked_tweet': 6666,
    },
    {
        'id': 5959,
        'user_name': "bobby",
        'liked_tweet': 7777,
    },
    {
        'id': 555,
        'user_name': "bob",
        'liked_tweet': 9999,
    },
    {
        'id': 559,
        'user_name': "bobE",
        'liked_tweet': 9999,
    }
]

results = []
seen = set()

for i in practice_json:

    obj = {'id': i['id'], 'user_name': i['user_name'], 'liked_tweet': i['liked_tweet']}

    if i['id'] in seen:
        continue

    else:
        results.append(obj)
        seen.add(i['id'])


for i in results:
    print(i)