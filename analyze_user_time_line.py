import os

import tweepy

from nrclex import NRCLex

import re
import nltk
import json
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# nltk.download('punkt') # Download nltk corpora
# nltk.download('wordnet')
# nltk.download('stopwords')
# nltk.download('omw-1.4')

from config import *


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=API_KEY,
                       consumer_secret=API_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_SECRET,
                       wait_on_rate_limit=True)


def pre_process(file_path):  # File path to raw './jsons/users_timeline_tweets/bob/bob_raw'

    stop_words = stopwords.words('english')

    lemmatizer = WordNetLemmatizer()

    lemmList = []

    results = []

    with open(file_path, 'r') as f:

        f_data = json.load(f)

        for tweet in f_data:

            #print(tweet['text'])
            #print()

            # removing punctuation & symbols
            tweet["text"] = re.sub(r'[^\w\s]', '', tweet["text"])

            # tokenization
            tweet['text'] = nltk.word_tokenize(tweet['text'])

            # removing stopwords
            for word in tweet['text']:
                if word in stop_words:
                    tweet['text'].remove(word)

            # removing http
            for word in tweet['text']:
                shortened = word[0:4]
                if shortened == 'http':
                    tweet['text'].remove(word)

            # removing gt
            for word in tweet['text']:
                if word == 'gt':
                    tweet['text'].remove(word)

            # removing date
            for word in tweet['text']:
                shortened = word[:1]
                if shortened == '0' or shortened == '1' or shortened == '2' or shortened == '3' or shortened == '4' or shortened == '5' or shortened == '6' or shortened == '7' or shortened == '8' or shortened == '9':
                    tweet['text'].remove(word)

            #print(tweet['text'])

            # lemmatization
            stemList = []
            for word in tweet['text']:
                stemList.append(lemmatizer.lemmatize(word))
            tweet['text'] = stemList
            stemList = []

            # pre-processed text
            #print(tweet['text'])
            #print()

            results.append(tweet)

        file_path_out = re.sub("\.json", "", file_path)

        with open(file_path_out+"_preprocessed.json", 'w+', encoding='utf-8') as j:
            json.dump(results, j, ensure_ascii=False, indent=4)


def emotional_analysis(file_path):  # File path to pre_processed './jsons/users_timeline_tweets/bob/bob_pre_processed'

    results = []

    with open(file_path, 'r') as f:
        f_data = json.load(f)

    text_object = NRCLex(file_path)

    for tweets in f_data:
        text_joined = NRCLex(' '.join(tweets['text']))

        obj = {'user_id': tweets['user_id'], 'tweet_id': tweets['tweet_id'], 'tweet_num': tweets['tweet_num'], 'text': tweets['text'],
               'raw_emotion_scores': text_joined.raw_emotion_scores, 'top_emotions': text_joined.top_emotions}

        results.append(obj)

    file_path_out = re.sub("_preprocessed.json", "", file_path)

    with open(file_path_out+'_analyzed.json','w+', encoding='utf-8') as j:
        json.dump(results, j, indent=4)


def user_average_emotion(file_path):

    results = []

    # each emotion points to the score and how many times it appears
    result = {'positive': 0, 'negative': 0, 'fear': 0, 'anger': 0, 'anticipation': 0, 'trust': 0, 'surprise': 0,
              'sadness': 0, 'disgust': 0, 'joy': 0}

    with open(file_path, 'r') as f:
        f_data = json.load(f)

        for tweet in f_data:
            for emotion in tweet["raw_emotion_scores"]:

                if emotion == "anticip":
                    emotion = "anticipation"

                result[emotion] += tweet["raw_emotion_scores"][emotion]

        result_avg = result.copy()

        if f_data:
            for emotion in result_avg:
                result_avg[emotion] /= len(f_data)
                # emotion /= len(f_data)
            results.append(result)
            results.append(result_avg)
            results.append({f_data[len(f_data) - 1]['tweet_num']})

        else:
            results = []



    file_path_out = re.sub("_analyzed.json", "", file_path)

    with open(file_path_out+"_average.json", 'w+') as f:
        json.dump(results, f, indent=4)

'''
        for tweet in f_data:
            for emotion in tweet["top_emotions"]:

                if emotion[0] == "anticip":
                    emotion[0] = "anticipation"

                result[emotion[0]][0] += emotion[1]

                result[emotion[0]][1] += 1

                print(emotion)

            print()


        print(result)
        for emotion in result:
            result[emotion][0] /= result[emotion][1]
            #emotion /= len(f_data)
        print("CORRECT")
        print(result)'''
        

def average_emotion_of_sign(filepath):

    results = []

    number_tweets = 0

    number_files = 0

    grand_total_avg = {'positive': 0, 'negative': 0, 'fear': 0, 'anger': 0, 'anticipation': 0, 'trust': 0, 'surprise': 0,
              'sadness': 0, 'disgust': 0, 'joy': 0}

    grand_total = {'positive': 0, 'negative': 0, 'fear': 0, 'anger': 0, 'anticipation': 0, 'trust': 0, 'surprise': 0,
              'sadness': 0, 'disgust': 0, 'joy': 0}

    for directory in os.listdir(filepath):
        if directory != ".DS_Store":
            with open(filepath+"/"+directory+"/"+directory+"_average.json", 'r') as f:
                f_data = json.load(f)

                if f_data:
                    for entry in f_data[1]:
                        grand_total_avg[entry] += f_data[1][entry]

                    for entry in f_data[0]:
                        grand_total[entry] += f_data[0][entry]

                    number_tweets += f_data[2]

                    number_files += 1

                else:
                    pass
                    #print("EMPTY")

    # AVERAGE
    for emotion in grand_total:
        grand_total_avg[emotion] /= number_files

    results.append(grand_total_avg)
    results.append(grand_total)
    results.append({'num_files': number_files})
    results.append({'num_tweets': number_tweets})

    output_filepath = "./jsons/grand_total_libra"

    # TO JSON
    with open(output_filepath+"/"+"libra_grand_average.json", 'w+') as f:
        json.dump(results, f, indent=4)


def main():

    filepath = "./jsons/users_timeline_tweets"

    for directory in os.listdir(filepath):
        if directory != ".DS_Store":
            filepath = "./jsons/users_timeline_tweets/"+directory+"/"+directory+".json"

            pre_process(filepath)

            emotional_analysis("./jsons/users_timeline_tweets/"+directory+"/"+directory+"_preprocessed.json")

            user_average_emotion("./jsons/users_timeline_tweets/"+directory+"/"+directory+"_analyzed.json")

    average_emotion_of_sign("./jsons/users_timeline_tweets")
    #average_emotion_of_sign("/Users/jacobkrawitz/Documents/GitHub/starstwitterbot/jsons/backup")


main()
