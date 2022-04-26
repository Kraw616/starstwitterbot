import json
import re

filepath = "./jsons/users_timeline_tweets/10/10.json"

print(filepath)

print(re.findall("/([0-9]+.json)", filepath))

filepath = re.sub(".json", "", filepath)

print(filepath)