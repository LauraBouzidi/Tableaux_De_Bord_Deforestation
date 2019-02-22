import os

path = "C:/Users/MARCU Quentin/Documents/Etudes/M1 SID/Scrapping/Articles_PMC"
dirs = os.listdir(path)


no_pertinent_1 = 0
no_pertinent_2 = 0
no_pertinent_3 = 0
no_pertinent_4 = 0
pertinent = 0

for file in dirs:
    article = open(path + "/" + file, 'r')
    checked = article.read()
    if('deforestation' not in checked):
        no_pertinent_1 += 1
    if('climate' not in checked):
        no_pertinent_2 += 1
    if('impact' not in checked or 'impacts' not in checked):
        no_pertinent_3 += 1
    if('deforestation' not in checked and 'climate' not in checked and ('impact' not in checked or 'impacts' not in checked)):
        no_pertinent_4 += 1
    if('deforestation' in checked and 'climate' in checked and ('impact' in checked or 'impacts' in checked)):
        pertinent += 1

print("\nNombre d'articles sans deforestation : " + str(no_pertinent_1))
print("Nombre d'articles sans climate : " + str(no_pertinent_2))
print("Nombre d'articles sans impact(s) : " + str(no_pertinent_3))
print("Nombre d'articles sans deforestation-climate-impact(s) : " + str(no_pertinent_4))
print("\nNombre d'articles avec deforestation-climate-impact(s) : " + str(pertinent))     