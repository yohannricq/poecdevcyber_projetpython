from typing import Optional
from src.models.compte import Compte
from src.dao.compte_dao import CompteDao


class CompteController:
    
    def __init__(self, compteDao: CompteDao) -> None:
        self.__compteDao = compteDao

    def save(self, compte: Compte) -> Compte:
        return self.__compteDao.save(compte)
    
    def find_by_id_utilisateur(self, id_utilisateur) -> Optional[Compte]:
        return self.__compteDao.find_by_id_utilisateur(id_utilisateur)
        
    @property
    def compteDao(self):
        return self.__compteDao
