CREATE DATABASE webs;
use webs;
create table if not exists login(
	log_id int(11) not null primary key auto_increment,
 	log_identifiant varchar(12) NOT NULL,
    	log_mdp varchar(100) not null 
);
