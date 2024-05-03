from src.controller.compte_controller import CompteController
from src.controller.utilisateur_controller import UtilisateurController
from src.dao.compte_dao import CompteDao
from src.dao.utilisateur_dao import UtilisateurDao
from src.config.my_connection import MyConnection
from src.view.interface_inscription import InterfaceInscription
from src.view.interface_connexion import InterfaceConnexion
from src.view.interface_accueil import InterfaceAccueil

myconnection = MyConnection()
if (myconnection.connection.is_connected):
    print("Connexion à la BDD")

    utilisateurDao = UtilisateurDao(myconnection)
    compteDao = CompteDao(myconnection)
    
    utilisateurController = UtilisateurController(utilisateurDao)
    compteController = CompteController(compteDao)
    
    # OK
    # interface_inscription = InterfaceInscription(utilisateurController, compteController)
    # interface_inscription.mainloop()

    #OK
    interface_connexion = InterfaceConnexion(utilisateurController, compteController)
    interface_connexion.mainloop()
    
    # interface_accueil = InterfaceAccueil(interface_connexion, interface_inscription)
    # interface_accueil.mainloop()

    myconnection.close()
    print("Déconnexion de la BDD")
else:
    print("Erreur de connexion à la BDD")
