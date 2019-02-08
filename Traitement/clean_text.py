# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 10:07:48 2019

@author: laura
"""


import random
import nltk
import numpy as np
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import os
import yaml

def sentense2cleanTokens(sent):
    #sent = sent.lower()
    sent = "".join([x if x.isalnum() else "" for x in sent])
    sent = " ".join(sent.split())
    return sent

def clean_words (sent):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(sent)
    filtered_sentence = [w for w in word_tokens if w not in stop_words]
    clean_sentence = []
    for sent2 in filtered_sentence:
        if sentense2cleanTokens(sent2) != "":
            clean_sentence.append(sentense2cleanTokens(sent2))
    return(clean_sentence)

path = "C:/Users/laura/Documents/M1/Tableau de bord/Articles_Natura/Articles_Natura/"
path2 = "C:/Users/laura/Documents/M1/Tableau de bord/Articles_Natura/Clean_Articles_Natura/"
doc = 'Natura_0.txt'

for doc in os.listdir(path):
    fichier = open(path + doc, encoding = "utf_8")
    text = fichier.read()
    fichier.close()
    dic = yaml.load(text)
    dic['title']=clean_words(dic['title'])
    dic['content']=clean_words(dic['content'])
    cont = ''
    title = ''
    for i in dic['content']:
        cont = cont + " " + i
    for j in dic['title']:
        title = title + " " + j
    dic['content'] = cont
    dic['title'] = title
    fichier1 = open(path2 + "clean_" + doc, "a", encoding = "utf_8")
    fichier1.write(str(dic))
    fichier1.close()
