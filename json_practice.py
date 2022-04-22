import json


with open('./jsons/libra_liked_users.json', encoding='utf-8', errors='ignore') as f:
    f2_data = json.load(f)

    dict = {}

    seen = set()

    for tweet_data in f2_data:
        seen.add(tweet_data['id'])
        if tweet_data['id'] in dict:
            dict[tweet_data['id']] += 1

        else:
            dict[tweet_data['id']] = 1

    '''for i in dict.keys():
        print("ID: " + str(i) + ", NUM FOUND: " + str(dict[i]))'''

    sorted_data = sorted(dict.items(), key=lambda x: x[1])#, reverse=True)

    print(sorted_data)

    for i in sorted_data:
        print(i[0], i[1])


# Create JSON with unique users and how many times we like
with open('./jsons/unique_liked_users.json', "w+") as file:
    pass  # TODO make json of all unique users


'''
results = []

for i in range(10):
    for j in range(50):

        obj = {'id': i, 'id2': j}
        results.append(obj)

        with open('./jsons/test1.json', 'w+') as f:
            json.dump(results, f, indent=4)


with open('./jsons/test1.json') as f:
    f_data = json.load(f)
    print(len(f_data))
'''