-- les pays les plus cité
select p.nom_pays, count(p.nom_pays) as occurence
from Articles a, Pays p, Concerne c
where a.Id_article = c.Id_article
and p.Id_pays = c.Id_pays
group by p.nom_pays;



--Pays vus negativement
select p.nom_pays, avg(a.sentiment) as sentiment_moyen
from Articles a, Pays p, Concerne c
where a.Id_article = c.Id_article
and p.Id_pays = c.Id_pays
and p.nom_pays In (select p.nom_pays
					from Articles a, Pays p, Concerne c
					where a.Id_article = c.Id_article
					and p.Id_pays = c.Id_pays
					group by p.nom_pays
					having count(p.nom_pays) > 3)
group by p.nom_pays
having avg(a.sentiment) < 0
order by sentiment_moyen;



--Pays vus positivement
select top(20) p.nom_pays, avg(a.sentiment) as sentiment_moyen
from Articles a, Pays p, Concerne c
where a.Id_article = c.Id_article
and p.Id_pays = c.Id_pays
and p.nom_pays In (select p.nom_pays
					from Articles a, Pays p, Concerne c
					where a.Id_article = c.Id_article
					and p.Id_pays = c.Id_pays
					group by p.nom_pays
					having count(p.nom_pays) > 3)
group by p.nom_pays
having avg(a.sentiment) > 0
order by sentiment_moyen desc;
;

--Pays dont parle le pays concerne(France)
select p1.nom_pays, count( p1.nom_pays) as nombre_article
from Articles a, Pays p1, Pays p2, Concerne c, Origine o
where c.Id_article = a.Id_article
and c.Id_pays = p1.Id_pays
and o.Id_article = a.Id_article
and o.Id_pays = p2.Id_pays
and o.Id_pays = (select Id_pays from pays where nom_pays = 'France')
group by p1.nom_pays
order by nombre_article desc;



--Pays qui parle du pays concerne(France)
select p2.nom_pays, count( p1.nom_pays) as nombre_article
from Articles a, Pays p1, Pays p2, Concerne c, Origine o
where c.Id_article = a.Id_article
and c.Id_pays = p1.Id_pays
and o.Id_article = a.Id_article
and o.Id_pays = p2.Id_pays
and c.Id_pays = (select Id_pays from pays where nom_pays = 'France')
group by p2.nom_pays
order by nombre_article desc;


--Occurences des mots clés

Select top(10) mc.mot, count(mc.mot) as nb_mot
From Mot_clefs mc, Comporte co
Where mc.id_mot = co.id_mot
Group by mc.mot
Order by nb_mot desc;

--L'auteur ayant écrit le plus d'articles

Select top(1) au.nom_auteur, count(au.nom_auteur) as nombre_article, avg(a.sentiment) as sentiment
From Auteurs au, Ecrit e, Articles a
Where au.id_auteur = e.id_auteur
and e.Id_article = a.Id_article
Group by au.nom_auteur
order by nombre_article desc;

--L'auteur le plus positif

Select top(1) au.nom_auteur, count(au.nom_auteur) as nombre_article, avg(a.sentiment) as sentiment
From Auteurs au, Ecrit e, Articles a
Where au.id_auteur = e.id_auteur
and e.Id_article = a.Id_article
and au.nom_auteur In (select au.nom_auteur
					from Articles a, Auteurs au, Ecrit e
					where a.Id_article = e.Id_article
					and au.Id_auteur = e.Id_auteur
					group by au.nom_auteur
					having count(e.Id_article) > 3)
Group by au.nom_auteur
order by sentiment desc;

--L'auteur le plus négatif

Select top(1) au.nom_auteur, count(au.nom_auteur) as nombre_article, avg(a.sentiment) as sentiment
From Auteurs au, Ecrit e, Articles a
Where au.id_auteur = e.id_auteur
and e.Id_article = a.Id_article
and au.nom_auteur In (select au.nom_auteur
					from Articles a, Auteurs au, Ecrit e
					where a.Id_article = e.Id_article
					and au.Id_auteur = e.Id_auteur
					group by au.nom_auteur
					having count(e.Id_article) > 3)
Group by au.nom_auteur
order by sentiment asc;

--Les mots clés sur la Chine

Select mc.mot, count(mc.mot) as occurences_chine
From Mot_clefs mc, Comporte co, Articles a, Concerne c, Pays p
Where mc.id_mot = co.id_mot
	And co.id_article = a.id_article
	And a.id_article = c.id_article
	And c.id_pays = p.id_pays
	And p.nom_pays = 'China'
Group by mc.mot
Order by occurences_chine desc;



-- analyse glorbal
-- les plus concerné par émissions de gas / par température / par species

Select p.nom_pays, count(co.id_article) as occurences
From Pays p, Concerne c, Articles a, Comporte co, Mot_clefs mc
Where p.id_pays = c.id_pays
	And c.id_article = a.id_article
	And a.id_article = co.id_article
	And co.id_mot = mc.id_mot
	And mc.mot = 'species'
Group by p.nom_pays
Order by occurences desc;
