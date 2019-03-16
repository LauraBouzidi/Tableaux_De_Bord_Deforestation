DROP TABLE Articles; 
DROP TABLE Mot_clefs; 
DROP TABLE Auteurs;
DROP TABLE Pays_origine_author; 
DROP TABLE Pays_content; 


ALTER TABLE Articles DROP PRIMARY KEY ;
ALTER TABLE Mot_clefs DROP PRIMARY KEY ;
ALTER TABLE Auteurs DROP PRIMARY KEY ;
ALTER TABLE Pays_content DROP PRIMARY KEY ;
ALTER TABLE Pays_origine_author DROP PRIMARY KEY ;



CREATE TABLE Articles (
    Id_article varchar(50) NOT NULL,
    Titre varchar(5000),
    date_article int,
	sentiment float
);

CREATE TABLE Mot_clefs (
    Id_article varchar(50) NOT NULL,
    mot varchar(50) NOT NULL
);

CREATE TABLE Pays_content (
    Id_article varchar(50) NOT NULL,
    nom_pays_content varchar(50) NOT NULL
);

CREATE TABLE Pays_origine_author (
    Id_article varchar(50) NOT NULL,
    nom_pays_origine_author varchar(50) NOT NULL
);

CREATE TABLE Auteurs (
    Id_article varchar(50) NOT NULL,
    nom_auteur varchar(100) NOT NULL
);







ALTER TABLE Articles 
   ADD CONSTRAINT PK_Articles PRIMARY KEY (Id_article);

ALTER TABLE Mot_clefs 
   ADD CONSTRAINT PK_Mot_clefs PRIMARY KEY (Id_article, mot);
ALTER TABLE Mot_clefs
   ADD CONSTRAINT FK_Mot_clefs FOREIGN KEY (Id_article) REFERENCES Articles (Id_article); 

ALTER TABLE Pays_content 
   ADD CONSTRAINT PK_Pays PRIMARY KEY (Id_article, nom_pays_content);
ALTER TABLE Pays_content
   ADD CONSTRAINT FK_Pays_content  FOREIGN KEY (Id_article) REFERENCES Articles (Id_article);

ALTER TABLE Pays_origine_author 
   ADD CONSTRAINT PK_Pays_origine_author PRIMARY KEY (Id_article, nom_pays_origine_author);
ALTER TABLE Pays_origine_author
   ADD CONSTRAINT FK_Pays_origine_author  FOREIGN KEY (Id_article) REFERENCES Articles (Id_article);

ALTER TABLE Auteurs 
   ADD CONSTRAINT PK_Auteurs PRIMARY KEY (Id_article, nom_auteur);
ALTER TABLE Auteurs
   ADD CONSTRAINT FK_Auteurs  FOREIGN KEY (Id_article) REFERENCES Articles (Id_article);
