import nltk
import pandas as pd
import os
import ast
import json
import pycountry
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')


path = "C:/Users/MARCU Quentin/Documents/Etudes/M1 SID/Scrapping/Articles_PMC"
dirs = os.listdir(path)

list_key_word = ["deforestation", "carbon", "greenhouse", "gas", "emissions",
                 "weather", "global warming", "fossil", "sea-level rise",
                 "temperature", "greed", "amenities", "habitat", "indigenous",
                 "flora", "species", "environment", "climate", "conducive",
                 "encroach", "forage", "destruction", "culture", "forest"]

for file in dirs:
    try:
        # Key Authors' countries
        article = open(path + "/" + file, 'r')
        checked = article.read()
        checked = ast.literal_eval(checked)
        list_country = list(set(checked.get("country")))
        checked['country'] = list_country
        
        # Key Article's countries
        title = checked.get("title")
        content = checked.get("content")
        list_country_article = []
        for country in pycountry.countries:
            if country.name in title or country.name in content:
                list_country_article.append(country.name)
        list_country_article = list(set(list_country_article))
        checked['country_quoted'] = list_country_article
        
        # Key Feelings
        nltk_sentiment = SentimentIntensityAnalyzer()
        sentence = checked['content']
        score = nltk_sentiment.polarity_scores(sentence)
        checked['feeling'] = score['compound']
        
        # Key Words
        key_words = []
        for key in list_key_word:
            if key in title or key in content:
                key_words.append(key)
        checked['key'] = key_words
        
        # Key id
        checked['id'] = file
        
        # New json
        with open('Documents/Etudes/M1 SID/Scrapping/Articles_PMC_2/' + file, 'w') as outfile:  
            json.dump(checked, outfile)
    except:
        print("error")
