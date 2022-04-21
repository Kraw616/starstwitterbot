import csv
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
#   nltk.download('punkt')
#   nltk.download('wordnet')
#   nltk.download('stopwords')
#   nltk.download('omw-1.4')

libraPosts = open("example_data/libraPosts.csv")

libraPreprocess = open("example_data/libraPreprocessed.csv", "w")

libraCsvReader = csv.reader(libraPosts)

libraCsvWriter = csv.writer(libraPreprocess)

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

libraPosts.close()
libraPreprocess.close()
