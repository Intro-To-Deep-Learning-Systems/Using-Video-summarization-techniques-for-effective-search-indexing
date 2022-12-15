import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import sys

def extract_keywords(text):
    print(text,file=sys.stderr)
    stop_words = set(stopwords.words('english'))
    word_tokens = []
    for i in text:
        word_tokens = word_tokens+word_tokenize(i)
    print(word_tokens,file=sys.stderr)
    filtered_sentence= [w for w in word_tokens if not w.lower() in stop_words]
    print(filtered_sentence,file=sys.stderr)
    filtered_sentence = set(filtered_sentence) 
    filtered_sentence = list(filtered_sentence)
    return filtered_sentence


# print(extract_keywords(["hi there","hello there"]))