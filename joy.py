import speech_recognition as sr
import pyttsx3
import datetime
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import random
import time
import string
import subprocess
import os
import json
import requests
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


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-us')
            print(f"user said:{statement}\n")

        except Exception as e:
            return "None"
        return statement

    speak("I am JOHN, University of Abuja Virtual assistant")


speak("i am created by the, computer science research team, under the guidance of, Dr. Hashim Bisallah")

wishMe()

if __name__ == '__main__':

    while True:
        # speak("Welcome Dr. Bisallah Hashim the H O D of computer science")
        # speak("Welcome Prof. Abdul-Rasheed Na'Allah the vice chancellor of University of Abuja")
       # speak("Tell me how can I help you?") or

        speak("How may i be of help?")
        print("How may i be of help?")

        statement = takeCommand().lower()
        if statement == 0:
            continue


speak('')

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
