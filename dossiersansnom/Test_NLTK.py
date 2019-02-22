# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 10:05:42 2019

@author: Damien
"""

import nltk
import csv
import pycountry

workpath = 'C:/Users/Damien/Downloads/Cours/INFO/Projet/Articles_Natura/'

f = open(workpath + 'Natura_0.txt')

data = f.readlines()

for line in data:
    tokens = nltk.word_tokenize(line)
    data2 = nltk.pos_tag(tokens)
    print(data2)
f.close()

NP = []
for word in data2:
    if 'NNP' in word[1]:
        NP.append(word[0])

with open(workpath+"nomPropre.csv", "w") as f_write:
    writer = csv.writer(f_write)
    for row in NP:
        writer.writerow(row)
        print(row)

for row in NP:
    for country in pycountry.countries:
        if country.name in row:
            print(row)
