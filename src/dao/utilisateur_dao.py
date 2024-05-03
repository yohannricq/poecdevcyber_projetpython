from typing import Optional
from src.config.my_connection import MyConnection
from .generic_dao import GenericDao
from src.models.utilisateur import Utilisateur


class UtilisateurDao (GenericDao[Utilisateur]):

    def __init__(self, connection_bdd: MyConnection) -> None:
        self.__connection_bdd = connection_bdd

    def save(self, utilisateur: Utilisateur) -> Utilisateur:
        insert = "INSERT INTO utilisateur(nom, prenom, email, mdp_actuel) VALUES(%s, %s, %s, %s);"
        values = (utilisateur.nom, utilisateur.prenom, utilisateur.email, utilisateur.mdp_actuel)
        print(f'Insert : {insert}, Values : {values}')
        self.__connection_bdd.query(insert, values)
        self.__connection_bdd.connection.commit()

    def find_by_email(self, email) -> Optional[Utilisateur]:
        select = 'SELECT * FROM utilisateur WHERE email = %s'
        values = [email]
        # values.append(email)
        return self.__connection_bdd.query(select, values).fetchone()
