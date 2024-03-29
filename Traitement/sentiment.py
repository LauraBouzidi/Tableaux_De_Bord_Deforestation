# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:46:54 2019

@author: theca
"""

import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
import os
import yaml

path = "C:/Users/theca/Desktop/scrapping/Nouveau dossier/Clean_Articles_Natura/"

dataset = []
for doc in os.listdir(path):
    fichier = open(path + doc, encoding = "utf_8")
    text = fichier.read()
    fichier.close()
    dic = yaml.load(text)
    dataset.append(dic['content'])
    

#dataset = ["Food is good and not too expensive. Serving is just right for adult. Ambient is nice too.",
#           "Used to be good. Chicken soup was below average, bbq used to be good.",
#           "Food was good, standouts were the spicy beef soup and seafood pancake! ",
#           "Good office lunch or after work place to go to with a big group as they have a lot of private areas with large tables",
#           "As a Korean person, it was very disappointing food quality and very pricey for what you get. I won't go back there again. ",
#           "Not great quality food for the price. Average food at premium prices really.",
#           "Fast service. Prices are reasonable and food is decent.",
#           "Extremely long waiting time. Food is decent but definitely not worth the wait.",
#           "Clean premises, tasty food. My family favourites are the clear Tom yum soup, stuffed chicken wings, chargrilled squid.",
#           "really good and authentic Thai food! in particular, we loved their tom yup clear soup with sliced fish. it's so well balanced that we can have it just on its own. "
#           ]


def nltk_sentiment(sentence):
    nltk_sentiment = SentimentIntensityAnalyzer()
    score = nltk_sentiment.polarity_scores(sentence)
    return score


nltk_results = [nltk_sentiment(row) for row in dataset]
nltk_results
results_df = pd.DataFrame(nltk_results)
results_df
text_df = pd.DataFrame(dataset, columns = ['text'])
text_df
nltk_df = text_df.join(results_df['compound'])
nltk_df

# compound > 0 : positive sentiment
# compound < 0 : negative sentiment

