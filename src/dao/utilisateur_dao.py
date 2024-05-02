from typing import Optional
from src.config.my_connection import MyConnection
from .generic_dao import GenericDao
from src.models.utilisateur import Utilisateur


class UtilisateurDao (GenericDao[Utilisateur]):

    def __init__(self, connection_bdd: MyConnection) -> None:
        self.__connection_bdd = connection_bdd

    def save(self, utilisateur: Utilisateur) -> Utilisateur:
        pass

    def find_by_email(self, email) -> Optional[Utilisateur]:
        select = 'SELECT * FROM utilisateur WHERE email = %s'
        values = []
        values.append(email)
        return self.__connection_bdd.query(select, values).fetchone()
