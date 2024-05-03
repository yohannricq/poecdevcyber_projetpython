from src.config.my_connection import MyConnection
from src.models.compte import Compte
from .generic_dao import GenericDao 


class CompteDao(GenericDao[Compte]):
    
    def __init__(self, connection_bdd: MyConnection) -> None:
        self.__connection_bdd = connection_bdd

    def save(self, compte: Compte) -> Compte:
        insert = "INSERT INTO compte(cle, sel, type, id_utilisateur) VALUES(%s, %s, %s, %s);"
        values = (compte.cle, compte.sel, compte.type, compte.id_utilisateur)
        print(f'Insert : {insert}, Values : {values}')
        self.__connection_bdd.query(insert, values)
        self.__connection_bdd.connection.commit()
        
    def find_by_id(self, id) -> Compte | None:
        pass