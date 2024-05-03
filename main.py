from src.controller.compte_controller import CompteController
from src.controller.utilisateur_controller import UtilisateurController
from src.dao.compte_dao import CompteDao
from src.dao.utilisateur_dao import UtilisateurDao
from src.config.my_connection import MyConnection
# from src.customcrypt import CustomCrypt
from src.view.interface_signup import InterfaceSignUp

# mdp = "formation"
# customCrypt = CustomCrypt(mdp)
# customCrypt.crypt()
# print(f'Mdp chiffré : {customCrypt.mdp_chiffre}')

myconnection = MyConnection()
if (myconnection.connection.is_connected):
    print("Connexion BDD OK")

    utilisateurDao = UtilisateurDao(myconnection)
    utilisateurController = UtilisateurController(utilisateurDao)
    
    compteDao = CompteDao(myconnection)
    compteController = CompteController(compteDao)

    form_signup = InterfaceSignUp(utilisateurController, compteController)
    form_signup.mainloop()

    myconnection.close()
    print("Fermeture connexion BDD")
else:
    print("Erreur connexion BDD")
