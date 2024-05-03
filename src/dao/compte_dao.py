from typing import Optional
from src.models.compte import Compte
from src.config.my_connection import MyConnection
from src.models.compte import Compte
from .generic_dao import GenericDao 


class CompteDao(GenericDao[Compte]):
    
    def __init__(self, connection_bdd: MyConnection) -> None:
        self.__connection_bdd = connection_bdd

    def save(self, compte: Compte) -> Compte:
        insert = "INSERT INTO compte(cle, sel, type, id_utilisateur) VALUES(%s, %s, %s, %s);"
        values = (compte.cle, compte.sel, compte.type, compte.id_utilisateur)
        print(f'insert : {insert}, values : {values}')
        self.__connection_bdd.query(insert, values)
        self.__connection_bdd.connection.commit()
        
    def find_by_id(self, id) -> Compte | None:
        pass
    
    def find_by_id_utilisateur(self, id_utilisateur) -> Optional[Compte]:
        select = 'SELECT * FROM compte WHERE id_utilisateur = %s'
        values = [id_utilisateur]
        return self.__connection_bdd.query(select, values).fetchone()
    
    