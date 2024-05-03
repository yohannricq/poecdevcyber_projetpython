CREATE TABLE utilisateur(
    id int PRIMARY KEY AUTO_INCREMENT,
    nom varchar(30),
    prenom varchar(30),
    email varchar(30),
    genre char(1),
    mdp_actuel varchar(30),
    mdp_precedent varchar(30),
    UNIQUE (email)
);

CREATE TABLE compte (
    id int PRIMARY KEY AUTO_INCREMENT,
    cle varchar(30),
    sel varchar(30),
    type varchar(3),
    id_utilisateur int,
    CONSTRAINT FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id)
);

INSERT INTO utilisateur(nom, prenom, email, mdp_actuel) VALUES('tata', 'tata', 'tata@gmail.com', 'tata');