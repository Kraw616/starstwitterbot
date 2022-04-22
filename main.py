import nltk
import re
import text2emotion as te
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import SpaceTokenizer
from nltk.tokenize import WhitespaceTokenizer
from nltk.tokenize.util import spans_to_relative
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nrclex import NRCLex

# Tokenize text into sentences

text1 = "Welcome readers. I hope you find it interesting. Please do reply."
print(sent_tokenize(text1))
print(te.get_emotion(text1))
text_object1 = NRCLex(text1)
print(text_object1.raw_emotion_scores)
print(text_object1.top_emotions, "\n")

# Tokenize sentences into words
text2 = "This is a test. I'm checking to see if I can tokenize these sentences. I hope it works."
print(word_tokenize(text2))
print(te.get_emotion(text2))
text_object2 = NRCLex(text2)
print(text_object2.raw_emotion_scores)
print(text_object2.top_emotions, "\n")

# Tokenize sentences into words using regular expressions
text3 = "I love computer science."
spaceRegExTok = RegexpTokenizer('\s+',gaps=True)
print(spaceRegExTok.tokenize(text3))
print(te.get_emotion(text3))
text_object3 = NRCLex(text3)
print(text_object3.raw_emotion_scores)
print(text_object3.top_emotions, "\n")

# Tokenize capitalized words using regular expressions
text4 = "This is so fun. Everyone is having a blast. Computer science class is the best."
capTok = RegexpTokenizer('[A-Z]\w+')
print(capTok.tokenize(text4))
print(te.get_emotion(text4))
text_object4 = NRCLex(text4)
print(text_object4.raw_emotion_scores)
print(text_object4.top_emotions, "\n")

# Tokenize characters or words split up by whitespaces
text5 = "I like dan ci n g"
spaceTok = SpaceTokenizer()
print(spaceTok.tokenize(text5))
print(te.get_emotion(text5))
text_object5 = NRCLex(text5)
print(text_object5.raw_emotion_scores)
print(text_object5.top_emotions, "\n")

# Returns the sequence of tuples that are offsets of the tokens
text6 = "I enjoy watching modern family, it is a very funny show."
print(list(WhitespaceTokenizer().span_tokenize(text6)))
print(te.get_emotion(text6))
text_object6 = NRCLex(text6)
print(text_object6.raw_emotion_scores)
print(text_object6.top_emotions, "\n")

# Returns the sequence of relative spans
text7 = "Although I enjoy watching modern family, my favorite TV show is called Bleach."
print(list(spans_to_relative(WhitespaceTokenizer().span_tokenize(text7))))
print(te.get_emotion(text7))
text_object7 = NRCLex(text7)
print(text_object7.raw_emotion_scores)
print(text_object7.top_emotions, "\n")

# Convert letters to lowercase and uppercase letters
text8 = "tHis is A TeST tO cHEck CaPAitAliZatIONs oR LaCK TherEoF."
print(text8.lower())
print(text8.upper())
print(te.get_emotion(text8))
text_object8 = NRCLex(text4)
print(text_object8.raw_emotion_scores)
print(text_object8.top_emotions, "\n")

# Print a list of the stop words included in the NLTK function
print(stopwords.words('english'), "\n")

# Return sentence with the stop words eliminated
text9 = "I want to go to the store to get food."
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(text9)
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
filtered_sentence = []
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
print(filtered_sentence, "\n")

# Stemming performed on a string
text10 = "Love Loves Lover Loving Lovers"
snowball = SnowballStemmer(language='english')
stemTok = word_tokenize(text10)
for w in stemTok:
    print(w, " : ", snowball.stem(w), "\n")


# Remove punctuations from text and tokenize sentence
text11 = '!hi. wh?at is the weat[h]er lik?e.'
noPunctString = re.sub(r'[^\w\s]', '', text11)
print(word_tokenize(noPunctString))











# text11 = "!hi. wh?at is the weat[h]er lik?e."
# from nltk.tokenize import WordPunctTokenizer
# print(WordPunctTokenizer(text11), "\n")






