from src.dao.utilisateur_dao import UtilisateurDao
from src.config.my_connection import MyConnection
from src.customcrypt import CustomCrypt
from src.view.form_signin import FormSignIn

mdp = "formation"
customCrypt = CustomCrypt(mdp)
customCrypt.crypt()
print(f'Mdp chiffré : {customCrypt.mdp_chiffre}')

myconnection = MyConnection()
if (myconnection.connection.is_connected):
    print("Connexion BDD OK")

    utilisateurDao = UtilisateurDao(myconnection)

    form_create_account = FormSignIn(utilisateurDao)
    form_create_account.mainloop()

    myconnection.close()
    print("Fermeture connexion BDD")
else:
    print("Erreur connexion BDD")
