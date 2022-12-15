import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import sys

def extract_keywords(text):
    print(text,file=sys.err)
    stop_words = set(stopwords.words('english'))
    print(stop_words,file=sys.err)
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    return filtered_sentence
