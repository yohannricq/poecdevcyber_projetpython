from tkinter import Button, Entry, Label, Tk, messagebox
from src.customcrypt import CustomCrypt
from src.models.utilisateur import Utilisateur
from src.dao.utilisateur_dao import UtilisateurDao


class FormSignUp(Tk):

    def __signup(self) -> None:

        nom = self.__entry_nom.get()
        prenom = self.__entry_prenom.get()
        email = self.__entry_email.get()
        mdp = self.__entry_mdp.get()

        # Si l'email existe déjà
        if self.__utilisateurDao.find_by_email(email) is not None:
            messagebox.showinfo(
                'Erreur inscription', 'Cette email existe déjà', icon=messagebox.ERROR)
        else:
            customcrypt = CustomCrypt(mdp)
            customcrypt.crypt()
            mdp = customcrypt.mdp_chiffre

            utilisateur = Utilisateur(nom, prenom, email, mdp)
            self.__utilisateurDao.save(utilisateur)
            messagebox.showinfo('Succes', 'Nouvel utilisateur inscrit', icon=messagebox.INFO)

            # if (res is not None):
            #     messagebox.showinfo('Message', 'Nouvel utilisateur inscrit', icon=messagebox.INFO)
            # else:
            #     messagebox.showinfo('Message', 'Erreur inscription utilisateur', icon=messagebox.ERROR)

    def __init__(self, utilisateurDao: UtilisateurDao) -> None:
        super().__init__()

        self.__utilisateurDao = utilisateurDao

        self.width = 500
        self.height = 500

        self.title('Inscription')
        self.geometry(f"{self.width}x{self.height}")

        label_nom = Label(self, text="Nom : ")
        label_nom.grid(row=0, column=0)

        self.__entry_nom = Entry(self)
        self.__entry_nom.grid(row=0, column=1)

        label_prenom = Label(self, text="Prenom : ")
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

        button_signup = Button(self, text="Valider", command=self.__signup)
        button_signup.place(x=83, y=95, height=20, width=100)
