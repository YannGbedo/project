CREATE DATABASE hids;
use hids;

CREATE TABLE IF NOT EXISTS conn_reff (
	co_id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	co_host varchar(250) NOT NULL,
	co_user varchar(250) NOT NULL,
	co_pwd varchar(250) NOT null
);

CREATE TABLE IF NOT EXISTS alerte (
	al_id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	al_titre varchar(100) NOT NULL,
	al_contenu varchar(100) NOT NULL,
	conn_id int(11) NOT null REFERENCES conn_reff (co_id)
);

create table if not exists `hashref` (
	`h_id` int(11) NOT NULL AUTO_INCREMENT primary key,
	`h_login` VARCHAR(12) NOT NULL,
    `h_mdp` varchar(100) NOT NULL
);
