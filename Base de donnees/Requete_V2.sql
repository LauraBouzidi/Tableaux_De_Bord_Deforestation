--1 OK
--Pays vus negativement
SELECT pc.nom_pays_content
FROM Articles a, Pays_content pc
WHERE a.id_article = pc.id_article
AND a.sentiment < 0
;

--2 OK
--Pays vus positivement
SELECT pc.nom_pays_content
FROM Articles a, Pays_content pc
WHERE a.id_article = pc.id_article
AND a.sentiment > 0
;

-- 3 OK
--Pays dont parle le pays concerne(Ajouter autres pays qui nous interessent)
SELECT pc.nom_pays_content 
FROM Pays_content pc, Articles a, Pays_origine_author po
WHERE po.nom_pays_origine_author = 'France'
AND a.id_article = pc.id_article
AND a.id_article = po.id_article
;

-- 4 FAUX /!\ NE RETOURNE QUE FRANCE
--Pays qui parle le pays concerne(Ajouter autres pays qui nous interessent)
SELECT pc.nom_pays_content 
FROM Pays_content pc, Articles a, Pays_origine_author po
WHERE pc.nom_pays_content = 'France'
AND a.id_article = pc.id_article
AND a.id_article = po.id_article
;

-- 5 OK
--Retourne les pays concernes et occurences
SELECT pc.nom_pays_content, COUNT(pc.id_article) as occurence
FROM Pays_content pc
GROUP BY pc.nom_pays_content
;

-- 6 OK
--Retourne les sentiments de l'auteur concerne
SELECT au.nom_auteur, AVG(a.sentiment) as sentiment
FROM Auteurs au, Articles a
WHERE au.id_article = a.id_article
GROUP BY au.nom_auteur
;

-- 7 OK
--Retourne les sentiments du pays concerne
SELECT pc.nom_pays_content, AVG(a.sentiment) as sentiment
FROM Pays_content pc, Articles a
WHERE pc.id_article = a.id_article
GROUP BY pc.nom_pays_content
;