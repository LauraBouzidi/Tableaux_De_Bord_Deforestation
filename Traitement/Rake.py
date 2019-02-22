# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 09:15:21 2019

@author: theca
"""

from rake_nltk import Rake, Metric
from nltk.corpus import stopwords
import pandas as pd
import os
import yaml

path = "C:/Users/theca/Desktop/scrapping/text/"

dataset = []
for doc in os.listdir(path):
    fichier = open(path + doc, encoding = "utf_8")
    text = fichier.read()
    fichier.close()
    dic = yaml.load(text)
    dataset.append(dic['content'])


r = Rake(max_length=4)


#print(dataset[0])
#test = "Fires related to Amazonian deforestation are a large source of particulate matter emissions. Satellite measurements and models reveal that reductions in deforestation and fire emissions since 2001 have prevented hundreds of premature deaths each year."
#test2 = "A significant challenge for policies aiming to reduce carbon emissions from deforestation is the avoidance of international carbon leakage. Research now shows, however, that even globally implemented forest conservation schemes could allow another type of carbon leakage through cropland expansion into non-forested areas."
#r.extract_keywords_from_text(test2)
#r.get_ranked_phrases()
#r.get_ranked_phrases_with_scores()


phrases_with_scores = []
for i in range(len(dataset)):
   r.extract_keywords_from_text(dataset[i])
   r.get_ranked_phrases()
   scor = r.get_ranked_phrases_with_scores()
   phrases_with_scores.append(scor)

print(phrases_with_scores)