import pycountry
import os

path = "C:/Users/MARCU Quentin/Documents/Etudes/M1 SID/Scrapping/Clean_Articles_PMC"
dirs = os.listdir(path)

dict_country = {}
for file in dirs:
    article = open(path + "/" + file, 'r', encoding="utf-8")
    text = article.read()
    for country in pycountry.countries:
        if country.name in text:
            if country.name in dict_country:
                dict_country[country.name].append(file)
            else:
                dict_country[country.name] = [file]
                
    article.close()