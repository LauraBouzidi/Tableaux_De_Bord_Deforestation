CREATE TABLE "articles" (
  "id_article" int,
  "titre" varchar,
  "date_article" date
);

CREATE TABLE "comporte" (
  "id_mot" int,
  "id_article" int
);

CREATE TABLE "zones" (
  "id_zone" int,
  "nom_zone" varchar
);

CREATE TABLE "concerne" (
  "id_zone" int,
  "id_article" int
);

CREATE TABLE "dates" (
  "annee" date
);

CREATE TABLE "mots_clef" (
  "id_mot" int,
  "mot" varchar
);

ALTER TABLE "dates" ADD FOREIGN KEY ("annee") REFERENCES "articles" ("date_article");

ALTER TABLE "articles" ADD FOREIGN KEY ("id_article") REFERENCES "concerne" ("id_article");

ALTER TABLE "zones" ADD FOREIGN KEY ("id_zone") REFERENCES "concerne" ("id_zone");

ALTER TABLE "articles" ADD FOREIGN KEY ("id_article") REFERENCES "comporte" ("id_article");

ALTER TABLE "mots_clef" ADD FOREIGN KEY ("id_mot") REFERENCES "comporte" ("id_mot");