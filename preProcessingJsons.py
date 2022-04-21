import csv
import re
import nltk
import json
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

#   nltk.download('punkt')
#   nltk.download('wordnet')
#   nltk.download('stopwords')
#   nltk.download('omw-1.4')

geminiPosts = open("example_data/geminiPosts.csv")
libraPosts = open("example_data/libraPosts.csv")

geminiPreprocess = open("example_data/geminiPreprocessed.csv", "w")
libraPreprocess = open("example_data/libraPreprocessed.csv", "w")

geminiCsvReader = csv.reader(geminiPosts)
libraCsvReader = csv.reader(libraPosts)

geminiCsvWriter = csv.writer(geminiPreprocess)
libraCsvWriter = csv.writer(libraPreprocess)

################################################################################

libraJsonData = json.loads("example_data/libra_tweets.json")
print(libraJsonData)





stop_words = stopwords.words('english')

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

stemList = []
lemmList = []

header = []

# so title is not processed
header = next(libraCsvReader)
libraCsvWriter.writerow(header)

header = next(libraCsvReader)



while (header != None):

    # original text
    print(header[1])
    print()

    # removing punctuation & symbols
    header[1] = re.sub(r'[^\w\s]','',header[1])

    # tokenization
    header[1] = nltk.word_tokenize(header[1])

    # removing stopwords
    for word in header[1]:
        if word in stop_words:
            header[1].remove(word)

    print(header[1])
    # stemming
    for word in header[1]:
        stemList.append(stemmer.stem(word))
    header[1] = stemList
    stemList = []

    print(header[1])
    # lemmatization
    for word in header[1]:
        stemList.append(lemmatizer.lemmatize(word))
    header[1] = stemList
    stemList = []

    # pre-processed text
    print(header[1])
    print()

    #
    libraCsvWriter.writerow(header)

    header = next(libraCsvReader)

geminiPosts.close()
libraPosts.close()
geminiPreprocess.close()
libraPreprocess.close()
