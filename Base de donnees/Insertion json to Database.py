# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 10:10:49 2019

@author: laura
"""

import pyodbc
import json
import os
import ast

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost\SQLEXPRESS;'
                      'Database=master;'
                      'Trusted_Connection=yes;')

json = {'title': ' Evaluating effectiveness conservation development investments reducing deforestation fires AnkenihenyZahemena Corridor Madagascar', 
        'author': ['Karyn Tabor', 'Kelly W. Jones', 'Jennifer Hewson', 'Andriambolantsoa Rasolohery', 'Andoniaina Rambeloson', 'Tokihenintsoa Andrianjohaninarivo', 'Celia A. Harvey'], 
        'country': ['Madagascar', 'United States'],
        'date': '2017',
        'content': ' Forest conservation REDD projects invest millions dollars year reduce local communities dependence forests prevent forest loss degradation However date limited evidence whether investments effective delivering conservation outcomes We explored relationships 600 smallscale conservation development investments occurred 2007 2014 conservation outcomes deforestation rates fire detections within AnkenihenyZahamena Corridor Madagascar using linear fixed effects panel regressions We derived annual changes forest cover fires satellite remote sensing We found statistically significant correlation presence investment reduced deforestation rates 2010 2011 years accelerated deforestation elsewhere study area This result indicated investments abated deforestation rates times political instability lack governance following 2009 coup Madagascar We also found statistically significant relationship presence investment reduced fire detections study area suggesting investments impact reducing burning forest agriculture For outcomes ie deforestation rates fire detections found dollars invested led greater conservation outcomes ie fewer fires less deforestation particularly funding sustained one two years Our findings suggest conservation development investments reduce deforestation fire incidence also highlight many challenges complexities assessing relationships investments conservation outcomes dynamic landscape volatile political context', 
        'country_quoted': ['Madagascar'],
        'feeling': 0.431,
        'key': ['deforestation', 'gas', 'culture', 'forest'],
        'id': 'PMC_1.txt'}


id_article = json['id']

for country in json['country_quoted']:
    get_id_country = conn.cursor()
    get_id_country.execute("Select Id_pays from master.dbo.Pays where nom_pays = '" + str(country) + "';")
    code = get_id_country[0]
    insert_country = conn.cursor()
    insert_country.execute("Insert Into master.dbo.Concerne Values ('" + str(id_article) + "','" + str(code) + "');")
    conn.commit()
    


for country in json['country']:
    get_id_country = conn.cursor()
    get_id_country.execute("Select Id_pays from master.dbo.Pays where nom_pays = '" + str(country) + "';")
    code = get_id_country[0]
    insert_country = conn.cursor()
    insert_country.execute("Insert Into master.dbo.origine Values ('" + str(id_article) + "','" + str(code) + "');")
    conn.commit()


for word in json['key']:
    get_id_key = conn.cursor()
    get_id_key.execute("Select Id_mot from master.dbo.Mots_clefs where mot = '" + str(word) + "';")
    code = get_id_key[0]
    insert_key_word = conn.cursor()
    insert_key_word.execute("Insert Into master.dbo.Comporte Values ('" + str(id_article) + "','" + str(code) + "');")
    conn.commit()


for author in json['author']:
    get_id_author = conn.cursor()
    get_id_author.execute("Select Id_mot from master.dbo.Auteurs where nom_auteur = '" + str(author) + "';")
    code = get_id_author[0]
    insert_author = conn.cursor()
    insert_author.execute("Insert Into master.dbo.Ecrit Values ('" + str(id_article) + "','" + str(code) + "');")
    conn.commit()