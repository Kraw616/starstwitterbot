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

geminiPosts = open("example_data/geminiPosts.csv")
geminiPreprocess = open("example_data/geminiPreprocessed.csv", "w")

geminiCsvReader = csv.reader(geminiPosts)

geminiCsvWriter = csv.writer(geminiPreprocess)

stop_words = stopwords.words('english')

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

stemList = []
lemmList = []

header = []

shortened = ""

# so title is not processed
header = next(geminiCsvReader)
geminiCsvWriter.writerow(header)

header = next(geminiCsvReader)



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

    # removing http
    for word in header[1]:
        shortened = word[0:4]
        if shortened == 'http':
            header[1].remove(word)

    # removing gt
    for word in header[1]:
        if word == 'gt':
            header[1].remove(word)

    # removing date
    for word in header[1]:
        shortened = word[:1]
        if shortened == '0':
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
    geminiCsvWriter.writerow(header)

    header = next(geminiCsvReader)

geminiPosts.close()
geminiPreprocess.close()
