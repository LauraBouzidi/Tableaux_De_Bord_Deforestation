# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 10:05:42 2019

@author: Damien
"""

import nltk
import pycountry
import wikipedia
import re

workpath = 'C:/Users/Damien/Downloads/Cours/INFO/Projet/Articles_Natura/'

f = open(workpath + 'Natura_0.txt')

data = f.readlines()

for line in data:
    tokens = nltk.word_tokenize(line)
    data2 = nltk.pos_tag(tokens)
f.close()

# Retourne les categories de tous les mots du texte

NP = []
for word in data2:
    if 'NNP' in word[1]:
        NP.append(word[0])
# with open(workpath+"nomPropre.csv", "w") as f_write:
#    writer = csv.writer(f_write)
#    for row in NP:
#        writer.writerow(row)
#        print(row)

for row in NP:
    for country in pycountry.countries:
        if country.name in row:
            print("1er test :" + row)

# places = GeoText(sentence)
# print places.cities

# Retourne les villes, pays et locations particulieres du texte

cities = []
countries = []
other_places = []
loc = []

for row in NP:
    summary = str(wikipedia.summary(row))
    if ('city' in summary):
        cities.append(row)
    elif ('country' in summary):
        countries.append(row)
    else:
        other_places.append(row)

for text in loc:
    other_places.append(text)

print("les villes:", cities)
print("les pays", countries)
print("autres locations", other_places)

# On retourne toutes les valeurs numeriques presentes dans le document

for line in data:
    cells = line.strip().split(',')
    b = ""
    for i in range(0, len(cells)):
        b += cells[i] + ','
    z = re.findall(r'\d+(?:\.\d+)?', b)
    print([float(z[s]) for s in range(len(z))])
