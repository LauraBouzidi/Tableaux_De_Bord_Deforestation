CREATE TABLE `articles` 
(
	`id_article` int,
	`titre` varchar(255),
	`date_article` date
);

CREATE TABLE `comporte` 
(
	`id_mot` int,
	`id_article` int
);

CREATE TABLE `pays` 
(
	`id_pays` int,
	`nom_pays` varchar(255)
);

CREATE TABLE `concerne` 
(
	`id_pays` int,
	`id_article` int
);

CREATE TABLE `mots_clef` 
(
	`id_mot` int,
	`mot` varchar(255)
);

CREATE TABLE `sentiments` 
(
	`id_sentiment` int,
	`sentiment` varchar(255)
);

CREATE TABLE `exprime` 
(
	`id_sentiment` int,
	`id_article` int
);

ALTER TABLE `articles` ADD FOREIGN KEY (`id_article`) REFERENCES `concerne` (`id_article`);

ALTER TABLE `pays` ADD FOREIGN KEY (`id_pays`) REFERENCES `concerne` (`id_pays`);

ALTER TABLE `articles` ADD FOREIGN KEY (`id_article`) REFERENCES `comporte` (`id_article`);

ALTER TABLE `mots_clef` ADD FOREIGN KEY (`id_mot`) REFERENCES `comporte` (`id_mot`);

ALTER TABLE `articles` ADD FOREIGN KEY (`id_article`) REFERENCES `exprime` (`id_article`);

ALTER TABLE `sentiments` ADD FOREIGN KEY (`id_sentiment`) REFERENCES `exprime` (`id_sentiment`);
