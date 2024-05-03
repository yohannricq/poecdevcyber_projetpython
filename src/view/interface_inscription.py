from tkinter import Button, Entry, Label, Tk, messagebox
from src.customcrypt import CustomCrypt
from src.controller.compte_controller import CompteController
from src.controller.utilisateur_controller import UtilisateurController
from src.models.compte import Compte
from src.models.utilisateur import Utilisateur
from src.conversion_functions import tuple_to_str


class InterfaceInscription(Tk):

    def __inscription(self) -> None:

        nom = self.__entry_nom.get()
        prenom = self.__entry_prenom.get()
        email = self.__entry_email.get()
        mdp = self.__entry_mdp.get()

        # Si l'email existe déjà
        if self.__utilisateur_controller.find_by_email(email) is not None:
            messagebox.showinfo('Erreur', 'Cet email existe déjà', icon=messagebox.ERROR)
        else:
            
            mdp = CustomCrypt.saler_mdp(mdp)
            cle = CustomCrypt.generer_cle(mdp)
            mdp_chiffre = CustomCrypt.crypt(mdp, cle)

            utilisateur = Utilisateur(nom, prenom, email, mdp_chiffre)
            self.__utilisateur_controller.save(utilisateur)
            
            id_utilisateur = self.__utilisateur_controller.get_last_id()
            
            cle = tuple_to_str(cle)
            print(f'tuple_to_str : {cle}')
            
            # Récupère le sel
            sel = ""
            index_start = int(len(mdp) / 2)
            for i in range(index_start, len(mdp), 1):
                sel += mdp[i]
                
            compte = Compte(cle, sel, 'new', id_utilisateur)
            self.__compte_controller.save(compte)
            
            messagebox.showinfo('Succes', 'Inscription réussie', icon=messagebox.INFO)

    def __init__(self, utilisateur_controller: UtilisateurController, compte_controller: CompteController) -> None:
        super().__init__()

        self.__utilisateur_controller = utilisateur_controller
        self.__compte_controller = compte_controller

        self.width = 500
        self.height = 500

        self.title('S\'inscrire')
        self.geometry(f"{self.width}x{self.height}")

        label_nom = Label(self, text="Nom : ")
        label_nom.grid(row=0, column=0)

        self.__entry_nom = Entry(self)
        self.__entry_nom.grid(row=0, column=1)

        label_prenom = Label(self, text="Prénom : ")
        label_prenom.grid(row=1, column=0)

        self.__entry_prenom = Entry(self)
        self.__entry_prenom.grid(row=1, column=1)

        label_email = Label(self, text="Email : ")
        label_email.grid(row=2, column=0)

        self.__entry_email = Entry(self)
        self.__entry_email.grid(row=2, column=1)

        label_mdp = Label(self, text="Mot de passe : ")
        label_mdp.grid(row=3, column=0)

        self.__entry_mdp = Entry(self)
        self.__entry_mdp.grid(row=3, column=1)

        button_signup = Button(self, text="Valider", command=self.__inscription)
        button_signup.place(x=83, y=95, height=20, width=100)
