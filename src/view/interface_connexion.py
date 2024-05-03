from tkinter import Button, Entry, Label, Tk, messagebox
from src.conversion_functions import str_to_tuple
from src.customcrypt import CustomCrypt
from src.controller.compte_controller import CompteController
from src.controller.utilisateur_controller import UtilisateurController


class InterfaceConnexion(Tk):

    def __connexion(self) -> None:
        email = self.__entry_email.get()
        mdp = self.__entry_password.get()

        utilisateur = self.__utilisateur_controller.find_by_email(email)

        if (utilisateur is not None):
            
            utilisateur = self.__utilisateur_controller.find_by_email(email)
            print(utilisateur)
            id_utilisateur = utilisateur[0]
            print(f'id utilisateur : {id_utilisateur}')
            
            compte = self.__compte_controller.find_by_id_utilisateur(id_utilisateur)
            print(compte)
            cle = compte[1]
            sel = compte[2]
            
            if(len(mdp) == len(sel)):
                
                tuple_cle = str_to_tuple(cle)
                print(f'tuple_cle : {tuple_cle}')
            
                mdp_chiffre = CustomCrypt.crypt(mdp + sel, tuple_cle)
            
                # Vérifie que le mdp chiffré est identique à celui en base
                if(mdp_chiffre == utilisateur[5]):
                    messagebox.showinfo('Succes', 'Connexion réussie', icon=messagebox.INFO)
                else:
                    messagebox.showinfo('Erreur', 'Le mot de passe est incorrect', icon=messagebox.ERROR)
            
            else:
                messagebox.showinfo('Erreur', 'Le mot de passe est incorrect', icon=messagebox.ERROR)
                
        else:
            messagebox.showinfo('Erreur', 'Cet email n\'appartient à aucun utilisateur', icon=messagebox.ERROR)

    def __init__(self, utilisateur_controller: UtilisateurController, compte_controller: CompteController) -> None:
        super().__init__()

        self.__utilisateur_controller = utilisateur_controller
        self.__compte_controller = compte_controller

        self.width = 500
        self.height = 500

        self.title('Se connecter')
        self.geometry(f"{self.width}x{self.height}")

        label_email = Label(self, text="Email : ")
        label_email.grid(row=0, column=0)

        self.__entry_email = Entry(self)
        self.__entry_email.grid(row=0, column=1)

        label_password = Label(self, text="Mot de passe : ")
        label_password.grid(row=1, column=0)

        self.__entry_password = Entry(self)
        self.__entry_password.grid(row=1, column=1)

        button_signup = Button(self, text="Valider", command=self.__connexion)
        button_signup.place(x=66, y=50, height=20, width=100)
