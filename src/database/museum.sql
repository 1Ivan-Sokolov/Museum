CREATE TABLE museum(
id INTEGER PRIMARY KEY,
name varchar(100) NOT NULL,
address varchar(100) NOT NULL
);

CREATE TABLE programm(
id integer PRIMARY KEY,
id_museum integer,
name varchar(100) NOT NULL,
date DATE NOT NULL,
description varchar(100) NOT NULL,
FOREIGN KEY(id_museum) REFERENCES museum(id)
	ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE tourguide(
id INTEGER PRIMARY KEY,
id_museum integer,
name varchar(100) NOT NULL,
FOREIGN KEY(id_museum) REFERENCES museum(id)
	ON DELETE SET NULL ON UPDATE NO ACTION
);


CREATE TABLE gallery(
id INTEGER PRIMARY KEY,
id_museum integer,
name varchar(100) NOT NULL,
FOREIGN KEY(id_museum) REFERENCES museum(id)
	ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE exhibition(
id INTEGER PRIMARY KEY,
id_museum integer,
name varchar(100) NOT NULL,
start_date datetime NOT NULL,
end_date DATEtime NOT NULL,
FOREIGN KEY(id_museum) REFERENCES museum(id)
	ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE visitor(
id INTEGER PRIMARY KEY,
name varchar(100) NOT NULL,
surname varchar(100) NOT NULL,
email varchar(100) NOT NULL,
contacts varchar(100) NOT NULL

);

CREATE TABLE ticket(
id INTEGER PRIMARY KEY,
id_museum integer,
id_exhibition integer,
id_visitor integer,
name varchar(100) NOT NULL,
date date NOT NULL,
time time NOT NULL,
ticket_price float(10, 2) NOT NULL,
FOREIGN KEY(id_museum) REFERENCES museum(id)
	ON DELETE CASCADE ON UPDATE NO ACTION,
  FOREIGN KEY(id_exhibition) REFERENCES exhibition(id)
	ON DELETE CASCADE ON UPDATE NO ACTION,
FOREIGN KEY(id_visitor) REFERENCES visitor(id)
	ON DELETE SET NULL ON UPDATE NO ACTION
);


CREATE TABLE exhibit(
id INTEGER PRIMARY KEY,
id_exhibition integer,
name varchar(100) NOT NULL,
category varchar(100) NOT NULL,
year_of_creation year NOT NULL,
author varchar(100) NOT NULL,
FOREIGN KEY(id_exhibition) REFERENCES exhibition(id)
	ON DELETE CASCADE ON UPDATE NO ACTION
 );

CREATE TABLE artwork(
id INTEGER PRIMARY KEY,
id_exhibition integer,
title varchar(100) NOT NULL,
year year  NOT NULL,
artist varchar(100) NOT NULL,
mediom varchar(100) NOT NULL,
description varchar(100) NOT NULL,
FOREIGN KEY(id_exhibition) REFERENCES exhibition(id)
	ON DELETE CASCADE ON UPDATE NO ACTION

);

CREATE TABLE review(
id INTEGER PRIMARY KEY,
id_exhibition integer,
id_visitor integer,
rating float NOT NULL,
comment varchar(100) NOT NULL,
FOREIGN KEY(id_exhibition) REFERENCES exhibition(id)
	ON DELETE CASCADE ON UPDATE NO ACTION,
  FOREIGN KEY(id_visitor) REFERENCES visitor(id)
	ON DELETE SET NULL ON UPDATE NO ACTION
)