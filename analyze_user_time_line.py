"""
Author: Jacob Krawitz, Jordan Wells, Alek DeMaio
Date: 5/10/22
Muhlenberg College 2022, Computer Science CUE

Description:

In this file, preprocessing and emotional analysis are performed to find 
the user's average emotional status and the average emotional scores for each given sign. 

"""

# import statements
import os
import tweepy
from nrclex import NRCLex
import re
import nltk
import json
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# download nltk corpa
# nltk.download('punkt') 
# nltk.download('wordnet')
# nltk.download('stopwords')
# nltk.download('omw-1.4')

# import the twitter developer creditentials
from config import *

# employ twitter developer creditentials
# CREATE TWEEPY OBJECT

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=API_KEY,
                       consumer_secret=API_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_SECRET,
                       wait_on_rate_limit=True)


'''
Method: pre_process()

Description: 

In this method, the collected tweet data is preprocessed and put into a .json file.

@params the filepath of the raw user tweets .json file
@returns preprocessed .json file

'''


def pre_process(file_path): 

    # set predefined stop words 
    stop_words = stopwords.words('english')

    # set lemmatizer 
    lemmatizer = WordNetLemmatizer()
  
    lemmList = []

    # create a list of results
    results = []

    # open and load the raw data .json file
    with open(file_path, 'r') as f:

        f_data = json.load(f)

        for tweet in f_data:

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

            # lemmatization
            stemList = []
            for word in tweet['text']:
                stemList.append(lemmatizer.lemmatize(word))
            tweet['text'] = stemList
            stemList = []
            
            # append the preproccessed tweets to the file
            results.append(tweet)

        file_path_out = re.sub("\.json", "", file_path)

        # write new preproccessed .json file
        with open(file_path_out+"_preprocessed.json", 'w+', encoding='utf-8') as j:
            json.dump(results, j, ensure_ascii=False, indent=4)

            
'''
Method: emotional_analysis()

Description: 

In this method, the preprocessed tweet data is used to perform emotional analysis and put into a .json file.

@params the filepath of the preprocessed user tweets .json file
@returns a .json file with the emotional profile of a user

'''
 
         
def emotional_analysis(file_path):

    # create list of results
    results = []

    #open and load preprocessed .json file
    with open(file_path, 'r') as f:
        f_data = json.load(f)

    # instantiate text object from .json file
    text_object = NRCLex(file_path)

    # join tokenized words
    for tweets in f_data:
        text_joined = NRCLex(' '.join(tweets['text']))

        # create dictionary with tweet infomation and associated emotional analysis
        obj = {'user_id': tweets['user_id'], 'tweet_id': tweets['tweet_id'], 'tweet_num': tweets['tweet_num'], 'text': tweets['text'],
               'raw_emotion_scores': text_joined.raw_emotion_scores, 'top_emotions': text_joined.top_emotions}

        # append each analysis to the file
        results.append(obj)

    file_path_out = re.sub("_preprocessed.json", "", file_path)

    # write new analyzed .json file
    with open(file_path_out+'_analyzed.json', 'w+', encoding='utf-8') as j:
        json.dump(results, j, indent=4)


'''
Method: user_average_emotion()

Description: 

In this method, the emotional analysis of each tweet is an average to give an average emotional profile for each user.

@params the filepath of the emotional analysis data for the user tweets .json file
'''


def user_average_emotion(file_path):

    results = list()

    # create dictionary for each emotion and how many times it appears
    result = {'positive': 0, 'negative': 0, 'fear': 0, 'anger': 0, 'anticipation': 0, 'trust': 0, 'surprise': 0,
              'sadness': 0, 'disgust': 0, 'joy': 0}

    # open the emotional analysis .json file
    with open(file_path, 'r') as f:
        f_data = json.load(f)

        # if emotion is found, add to the count
        for tweet in f_data:
            for emotion in tweet["raw_emotion_scores"]:

                if emotion == "anticip":
                    emotion = "anticipation"

                result[emotion] += tweet["raw_emotion_scores"][emotion]

        # create copy of results
        result_avg = result.copy()

        # divide by length of f_data (number of tweets) to find average of each emotion for the user
        if f_data:
            for emotion in result_avg:
                result_avg[emotion] /= len(f_data)
                
            # append the results
            results.append(result)
            
            # append the average for each emotion
            results.append(result_avg)
            
            # append the number of tweets
            results.append({'num_tweets': f_data[len(f_data) - 1]['tweet_num']})

        else:
            results = []

    file_path_out = re.sub("_analyzed.json", "", file_path)

    # write new average emotional analysis .json file
    with open(file_path_out+"_average.json", 'w+') as f:
        json.dump(results, f, indent=4)
    
    
'''
Method: average_emotion_of_sign()

Description: 

In this method, the average emotional profile of each user is averaged to give an average emotional profile for each sign.
Outputted to the grand_total.json file is:

[0] = The total counts for the sign
[1] = The average emotion word count per user
[2] = The average emotion word count per tweet
[3] = The proportion of emotions in an average tweet from this sign
[4] = The number of users analyzed in this sign
[5] = The number of tweets analyzed in this sign

@params the filepath of the folder that contains a given sign's user timeline collected tweet data , what sign we are getting the average for
@returns a _grand_average.json file for a given sign

'''


def average_emotion_of_sign(filepath, sign):

    # create list of results
    results = []

    # set the number of tweets to 0
    number_tweets = 0

    # set the number of files to 0
    number_files = 0

    #set the proportion to 0
    total_prop = 0

    # create dictionary for the total count of each emotion for the entire zodiac sign
    grand_total_count = {'positive': 0, 'negative': 0, 'fear': 0, 'anger': 0, 'anticipation': 0, 'trust': 0, 'surprise': 0,
              'sadness': 0, 'disgust': 0, 'joy': 0}

    # open and load emotional analysis average .json files for a given sign
    for directory in os.listdir(filepath):
        if directory != ".DS_Store":    # Hidden file causes errors
            with open(filepath+"/"+directory+"/"+directory+"_average.json", 'r') as f:
                f_data = json.load(f)

                if f_data:
                    # count the total of each count for each emotion
                    for entry in f_data[0]:
                        grand_total_count[entry] += f_data[0][entry]

                    # count the number of tweets
                    number_tweets += f_data[2]['num_tweets']

                    # count the number of files
                    number_files += 1

    # create dictionaries to hold the average count of words per user and average count of emotion word per tweet
    grand_avg_count_user = grand_total_count.copy()
    grand_avg_count_tweet = grand_total_count.copy()

    # divide by the number of users to find the average count of emotion words per user
    for emotion in grand_avg_count_user:
        grand_avg_count_user[emotion] /= number_files

    # divide by the number of tweets to find the average total emotion word count per tweet
    for emotion in grand_avg_count_tweet:
        grand_avg_count_tweet[emotion] /= number_tweets
    
    # create dictionary to hold the proportions of emotions for each tweet
    grand_total_proportion = grand_avg_count_tweet.copy()

    # generate the denominator (the whole) to get the proportion of each emotion per tweet
    for emotion in grand_total_proportion:
        total_prop += grand_total_proportion[emotion]

    # divide by the total proportion (the whole) to get the proportion of each emotion to each other
    for emotion in grand_total_proportion:
        grand_total_proportion[emotion] /= total_prop

    # append averages to the list to be outputted to the out file
    results.append(grand_total_count)     # results[0] = Total words that trigger each emotion per sign
    results.append(grand_avg_count_user)   # results[1] = Average count of emotion words per user
    results.append(grand_avg_count_tweet)   # results[2] = Average count of emotion words per tweet (of this sign)
    results.append(grand_total_proportion)  # results[3] = Proportion of each emotion in a tweet typical of this sign
    results.append({'num_files': number_files})  # results[4] = number of files (users) analyzed
    results.append({'num_tweets': number_tweets})   # results[5] = number of tweets analyzed

    output_filepath = "./jsons/grand_totals/"

    # write the grand averages .json file
    with open(output_filepath+"/"+sign+"_grand_average.json", 'w+') as f:
        json.dump(results, f, indent=4)


'''
Method: main()

Description: Main driver of the file. First, assign a flag that says what sign you wish to analyze. Then, sets a filepath
that leads to the tweet data for the users of the given sign. For each of these users, preprocess the raw tweet.json,
creating a pre_processed.json version of their tweets. Then, perform emotional analysis on this pre_processed.json file.
Finally, creates an average "emotional profile" for each user. After this loop, generates a file that lists grand totals/
final emotional profile for the given sign.

'''


def main():

    # assign the zodiac sign (need to run this file once for each sign, changed this flag0
    sign = 'libra'

    '''
    'libra'
    'gemini'
    'aries'
    'taurus'
    'cancer'
    'leo'
    'virgo'
    'scorpio'
    'sagittarius'	
    'capricorn'
    'aquarius'	
    'pisces'
    '''

    filepath = "./jsons/users_timeline_tweets/"+sign

    for directory in os.listdir(filepath):
        if directory != ".DS_Store":
            filepath = "./jsons/users_timeline_tweets/"+sign+'/'+directory+"/"+directory+".json"
            
            # call the preprocess method
            pre_process(filepath)

            # call the emotional analysis method
            emotional_analysis("./jsons/users_timeline_tweets/"+sign+'/'+directory+"/"+directory+"_preprocessed.json")

            # call the user average emotion method
            user_average_emotion("./jsons/users_timeline_tweets/"+sign+'/'+directory+"/"+directory+"_analyzed.json")
    
    # call the average emotion of sign method
    average_emotion_of_sign("./jsons/users_timeline_tweets/"+sign, sign)


# call the main method
main()
