from typing import Optional
from src.models.utilisateur import Utilisateur
from src.dao.utilisateur_dao import UtilisateurDao


class UtilisateurController:
    
    def __init__(self, utilisateurDao: UtilisateurDao) -> None:
        self.__utilisateurDao = utilisateurDao

    def save(self, utilisateur: Utilisateur) -> Utilisateur:
        self.__utilisateurDao.save(utilisateur)
        
    def find_by_email(self, email) -> Optional[Utilisateur]:
        return self.__utilisateurDao.find_by_email(email)
    
    def find_by_id(self, id) -> Utilisateur | None:
        return self.__utilisateurDao.find_by_id(id)
    
    def get_last_id(self) -> int:
        return self.__utilisateurDao.connection_bdd.cursor._last_insert_id
        
    @property
    def utilisateurDao(self):
        return self.__utilisateurDao

    @utilisateurDao.setter
    def utilisateurDao(self, value):
        self.__utilisateurDao = value
