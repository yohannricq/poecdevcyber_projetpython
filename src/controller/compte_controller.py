from src.models.compte import Compte
from src.models.utilisateur import Utilisateur
from src.dao.compte_dao import CompteDao


class CompteController:
    
    def __init__(self, utilisateurDao: CompteDao) -> None:
        self.__compteDao = utilisateurDao

    def save(self, compte: Compte) -> Utilisateur:
        self.__compteDao.save(compte)
        
    @property
    def compteDao(self):
        return self.__compteDao

    @compteDao.setter
    def compteDao(self, value):
        self.__compteDao = value
