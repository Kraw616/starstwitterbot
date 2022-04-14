import json

tweet = [{
    'id': "1555051",
    'text': "I love Libras!",
    'author_name': "BotLover"
}]

string = json.dumps(tweet, indent=2)

with open('test.json', 'w') as outfile:
    outfile.write(string)

tweet2 = {
    'id': "1555052",
    'text': "I hate Libras!",
    'author_name': "BotLover2"
}

print(string)
with open('test.json') as f:
    data = json.load(f)

data.append(tweet2)
print(data)

with open('test2.json', 'w') as out:
    json.dump(data, out,indent=4)


