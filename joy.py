from sklearn.metrics.pairwise import cosine_similarity, linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import random
import string
import re
import string
import unicodedata
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
import wikipedia as wk
from collections import defaultdict
import warnings
warnings.filterwarnings("ignore")
nltk.download('punkt')
nltk.download('wordnet')

data = open('/../../Document/HR.txt', 'r', errors='ignore')
raw = data.read()
raw = raw.lower()


raw[:1000]
'human resource management is the process of recruiting, selecting, inducting employees, providing orientation, imparting training and development, appraising the performance of employees, deciding compensation and providing benefits, motivating employees, maintaining proper relations with employees and their trade unions, ensuring employees safety, welfare and healthy measures in compliance with labour laws of the land.\nhuman resource management involves management functions like planning, organizing, directing and controlling\nit involves procurement, development, maintenance of human resource\nit helps to achieve individual, organizational and social objectives\nhuman resource management is a multidisciplinary subject. it includes the study of management, psychology, communication, economics and sociology.\nit involves team spirit and team work.\nit is a continuous process.\nhuman resource management as a department in an organisation handles all aspects of employees and has various functi'

sent_tokens = nltk.sent_tokenize(raw)


def Normalize(text):
    remove_punct_dict = dict((ord(punct), None)
                             for punct in string.punctuation)
    # word tokenization
    word_token = nltk.word_tokenize(text.lower().translate(remove_punct_dict))

    # remove ascii
    new_words = []
    for word in word_token:
        new_word = unicodedata.normalize('NFKD', word).encode(
            'ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)

    # Remove tags
    rmv = []
    for w in new_words:
        text = re.sub("&lt;/?.*?&gt;", "&lt;&gt;", w)
        rmv.append(text)

    # pos tagging and lemmatization
    tag_map = defaultdict(lambda: wn.NOUN)
    tag_map['J'] = wn.ADJ
    tag_map['V'] = wn.VERB
    tag_map['R'] = wn.ADV
    lmtzr = WordNetLemmatizer()
    lemma_list = []
    rmv = [i for i in rmv if i]
    for token, tag in nltk.pos_tag(rmv):
        lemma = lmtzr.lemmatize(token, tag_map[tag[0]])
        lemma_list.append(lemma)
    return lemma_list


welcome_input = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
welcome_response = ["hi", "hey", "*nods*", "hi there",
                    "hello", "I am glad! You are talking to me"]


def welcome(user_response):
    for word in user_response.split():
        if word.lower() in welcome_input:
            return random.choice(welcome_response)


def generateResponse(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=Normalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    #vals = cosine_similarity(tfidf[-1], tfidf)
    vals = linear_kernel(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf == 0) or "tell me about" in user_response:
        print("Checking Wikipedia")
        if user_response:
            robo_response = wikipedia_data(user_response)
            return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response  # wikipedia search


def wikipedia_data(input):
    reg_ex = re.search('tell me about (.*)', input)
    try:
        if reg_ex:
            topic = reg_ex.group(1)
            wiki = wk.summary(topic, sentences=3)
            return wiki
    except Exception as e:
        print("No content has been found")

        flag = True


print("My name is Joy and I'm a intelligent virtual robot. If you want to exit, type Bye!")
while(flag == True):
    user_response = input()
    user_response = user_response.lower()
    if(user_response not in ['bye', 'shutdown', 'exit', 'quit']):
        if(user_response == 'thanks' or user_response == 'thank you'):
            flag = False
            print("Chatterbot : You are welcome..")
        else:
            if(welcome(user_response) != None):
                print("Chatterbot : "+welcome(user_response))
            else:
                print("Chatterbot : ", end="")
                print(generateResponse(user_response))
                sent_tokens.remove(user_response)
    else:
        flag = False
        print("Chatterbot : Bye!!! ")
