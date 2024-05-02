from tkinter import Button, Entry, Label, Tk, messagebox
from src.dao.utilisateur_dao import UtilisateurDao


class FormSignIn(Tk):

    def __signin(self) -> None:
        email = self.__entry_username.get()

        utilisateur = self.__utilisateurDao.find_by_email(email)

        if (utilisateur is not None):
            messagebox.showinfo(
                'Message', 'Utilisateur trouvé en BDD', icon=messagebox.INFO)
        else:
            messagebox.showinfo(
                'Message', 'Utilisateur non trouvé en BDD', icon=messagebox.ERROR)

    def __init__(self, utilisateurDao: UtilisateurDao) -> None:
        super().__init__()

        self.__utilisateurDao = utilisateurDao

        self.width = 500
        self.height = 500

        self.title('Accueil')
        self.geometry(f"{self.width}x{self.height}")

        label_username = Label(self, text="Username : ")
        label_username.grid(row=0, column=0)

        self.__entry_username = Entry(self)
        self.__entry_username.grid(row=0, column=1)

        label_password = Label(self, text="Password : ")
        label_password.grid(row=1, column=0)

        self.__entry_password = Entry(self)
        self.__entry_password.grid(row=1, column=1)

        button_signup = Button(self, text="Sign in", command=self.__signin)
        button_signup.place(x=66, y=50, height=20, width=100)
