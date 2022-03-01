from nltk.corpus import stopwords
from nltk.tokenize import regexp_tokenize
from string import punctuation
import math


# Filter the least important words and special characters/punctuation
def filtering_words(doc):
    stop_words = set(stopwords.words("english"))
 # 'Tokenizing' every word
    token_text = regexp_tokenize(doc, "[\w']+")
 # Set of special characters
    special_characters = set(punctuation)
 # Setting the important words in lower removing every special word and stopword 
    filtered_text = [word.lower() for word in token_text if word.lower() not in stop_words and word.lower() not in special_characters]
    return filtered_text


 #Setting up the dictionary DS
def count_words(doc):
    dict = {}
    for i in range(len(doc)):
        if doc[i] in dict:
           dict[doc[i]] += 1
        else:
           dict[doc[i]] = 1
    return dict

def dot_product(doc1, doc2):
    sum = 0
    for key in doc1:
        if key in doc2:
            sum += (doc1[key] * doc2[key])
    return sum

def vector_angle(d1,d2):
    numerator = dot_product(d1, d2)
    denominator = math.sqrt(dot_product(d1, d1)*dot_product(d2, d2))
      
    return math.acos(numerator / denominator)


string1 = "This is a test so we can now what is the similarity between this two things"
string2 = "This is a test so we can now what is the similarity between this two things"

filtered1 = filtering_words(string1)
filtered2 = filtering_words(string2)

counter1 = count_words(filtered1)
counter2 = count_words(filtered2)

distance = vector_angle(counter1, counter2)
print("The distance between the documents is: % 0.6f (radians)"% distance)









            















