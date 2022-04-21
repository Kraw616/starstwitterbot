import csv
import re
import nltk
import json
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

#nltk.download('punkt')
#nltk.download('wordnet')
#nltk.download('stopwords')
#nltk.download('omw-1.4')



################################################################################

#libraJsonData = json.loads("example_data/libra_tweets.json")
#print(libraJsonData)

stop_words = stopwords.words('english')

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

stemList = []
lemmList = []


file_path = "example_data/libra_tweets.json"

with open(file_path, 'r') as j:
    header = json.loads(j.read())
    #print(header[0]["text"])


    while_ptr = 0


    while(while_ptr<len(header)):
        # original text
        print(header[while_ptr]["text"])
        print()

        # removing punctuation & symbols
        header[while_ptr]["text"] = re.sub(r'[^\w\s]','',header[while_ptr]["text"])

        # tokenization
        header[while_ptr]["text"] = nltk.word_tokenize(header[while_ptr]["text"])

        # removing stopwords
        for word in header[while_ptr]["text"]:
            if word in stop_words:
                header[while_ptr]["text"].remove(word)

        # removing http
        for word in header[while_ptr]["text"]:
            shortened = word[0:4]
            if shortened == 'http':
                header[while_ptr]["text"].remove(word)

        # removing gt
        for word in header[while_ptr]["text"]:
            if word == 'gt':
                header[while_ptr]["text"].remove(word)

        # removing date
        for word in header[while_ptr]["text"]:
            shortened = word[:1]
            if shortened == '0' or shortened == '1' or shortened == '2' or shortened == '3' or shortened == '4' or shortened == '5' or shortened == '6' or shortened == '7' or shortened == '8' or shortened == '9':
                header[while_ptr]["text"].remove(word)

        print(header[while_ptr]["text"])
        # stemming
        for word in header[while_ptr]["text"]:
            stemList.append(stemmer.stem(word))
        header[while_ptr]["text"] = stemList
        stemList = []

        print(header[while_ptr]["text"])
        # lemmatization
        for word in header[while_ptr]["text"]:
            stemList.append(lemmatizer.lemmatize(word))
        header[while_ptr]["text"] = stemList
        stemList = []

        # pre-processed text
        print(header[while_ptr]["text"])
        print()

        #
        #libraCsvWriter.writerow(header)

        #header = next(libraCsvReader)
        while_ptr+=1
        #print("one iteration")

with open('example_data/libra_preprocessed.json', 'w', encoding='utf-8') as f:
    json.dump(header, f, ensure_ascii=False, indent=4)
