import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import SpaceTokenizer
from nltk.tokenize import WhitespaceTokenizer
from nltk.tokenize.util import spans_to_relative
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

# Open the file
file1 = open('libraPosts.txt', 'r')
# Set count to 0
count = 0

# Loop until end of the file
while True:
    # Add one to count for every line that is read
    count += 1

    # Read the next line in the file
    line = file1.readline()

    # Break once the end of the file is reached
    if not line:
        break
    # Print tokenized line of text
    print("Line{}: {}".format(count, word_tokenize(line.strip())))

# Close the file
file1.close()