class Utilisateur:

    def __init__(self, nom: str, prenom: str, email: str) -> None:
        self.__nom = nom
        self.__prenom = prenom
        self.__email = email

    @property
    def _nom(self):
        return self.__nom

    @_nom.setter
    def _nom(self, value):
        self.__nom = value

    @property
    def _prenom(self):
        return self.__prenom

    @_prenom.setter
    def _prenom(self, value):
        self.__prenom = value

    @property
    def _email(self):
        return self.__email

    @_email.setter
    def _email(self, value):
        self.__email = value
