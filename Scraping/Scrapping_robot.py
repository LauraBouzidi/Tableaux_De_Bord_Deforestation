import requests
from bs4 import BeautifulSoup
import json


def articles():
    pages = []
    for i in range(1, 19):
        pages.append(requests.get("https://www.nature.com/search?q=deforestation+climate+impact&order=relevance&page=" + str(i)))
    for i in range(len(pages)):
        pages[i] = BeautifulSoup(pages[i].content, 'html.parser')
    return pages


def articlesPerPage(pages):
    links = []
    for article in pages.find_all('h2', attrs={'class': 'h3 extra-tight-line-height'}):
        for link in article.find_all('a'):
            linkfound = link.get('href')
            links.append("https://www.nature.com" + linkfound)
    links = set(links)
    return links


def find_title(page):
    page = BeautifulSoup(page.content, 'html.parser')
    for article in page.find_all('meta', attrs={'name': 'dc.title'}):
        title = article.get('content')
    return title


def find_date(page):
    page = BeautifulSoup(page.content, 'html.parser')
    for article in page.find_all('meta', attrs={'name': 'dc.date'}):
        date = article.get('content')
    return date


def find_text(page):
    page = BeautifulSoup(page.content, 'html.parser')
    for article in page.find_all('meta', attrs={'name': 'dc.description'}):
        text = article.get('content')
    return text


def articleContent(pages):
    articles = []
    for i in range(len(pages)):
        articles.append(articlesPerPage(pages[i]))
    article = []
    for i in range(len(articles)):
        for j in articles[i]:
            article.append(requests.get(j))
    for i in range(len(article)):
        try:
            title = find_title(article[i])
            date = find_date(article[i])
            text = find_text(article[i])
            dict_article = {'title': title, 'date': date, 'content': text}
            with open('Documents/Etudes/M1 SID/Scrapping/Articles_Natura/Natura_'+str(i)+'.txt', 'w') as outfile:  
                json.dump(dict_article, outfile)
            print(i)
        except:
            print("Error : " + str(i))


pages = articles()
articleContent(pages)
