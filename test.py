from nrclex import NRCLex
import json

with open("./jsons/grand_total_libra/libra_grand_average.json", 'r') as f:
    f_data = json.load(f)


prop_libra = dict()
test_prop = dict()
test_total = 0

results = []

for emotion in f_data[3]:
    prop_libra[emotion] = f_data[3][emotion]

prop_gemini = {'positive': .5, 'negative': .125, 'fear': .6, 'anger': .12, 'anticipation': .06, 'trust': .43, 'surprise': .01,
          'sadness': .07, 'disgust': 0.06, 'joy': 0.2}

prop_all = {'positive': [], 'negative': [], 'fear': [], 'anger': [], 'anticipation': [], 'trust': [], 'surprise': [],
          'sadness': [], 'disgust': [], 'joy': []}


input = "I am intelligent, funny, inquisitive, and thoughtful. Love Tweet. I am angry and sad"


obj = NRCLex(input)

for emotion in obj.raw_emotion_scores:

    test_total += obj.raw_emotion_scores[emotion]

for emotion in prop_gemini:#obj.raw_emotion_scores:
    if emotion in obj.raw_emotion_scores:
        test_prop[emotion] = obj.raw_emotion_scores[emotion] / test_total
    else:
        test_prop[emotion] = 0


for emotion in prop_all:
    prop_all[emotion].append(prop_gemini[emotion])
    prop_all[emotion].append(prop_libra[emotion])

for emotion in test_prop:
    if emotion in prop_all:
        output = min(prop_all[emotion], key=lambda x: abs(x-test_prop[emotion]))

        results.append({emotion: output})

libra_count = 0
gem_count = 0
counts = []

for i in results:
    for emotion in i:
        if i[emotion] == prop_libra[emotion]:
            i[emotion] = 'LIBRA'
            libra_count += 1
        elif i[emotion] == prop_gemini[emotion]:
            i[emotion] = 'GEMINI'
            gem_count += 1

counts.append(libra_count)
counts.append(gem_count)

final_verdict = counts.index(max(counts))


#print(obj.raw_emotion_scores)
print(test_prop)
#print(prop_libra)
#print(prop_gemini)
print(prop_all)
print(results)


if final_verdict == 0:
    print("LIBRA")
elif final_verdict == 1:
    print("GEMINI")


# 2.91508269724
# pos = 0.19180811841
# neg = 0.1439192549
# fear = 0.07434873959
# anger =
