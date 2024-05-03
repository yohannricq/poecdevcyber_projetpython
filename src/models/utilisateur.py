class Utilisateur:

    def __init__(self, nom: str, prenom: str, email: str, mdp_actuel: str) -> None:
        self.__nom = nom
        self.__prenom = prenom
        self.__email = email
        self.__mdp_actuel = mdp_actuel

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def _nom(self, value):
        self.__nom = value

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, value):
        self.__prenom = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def mdp_actuel(self):
        return self.__mdp_actuel

    @mdp_actuel.setter
    def _mdp_actuel(self, value):
        self.__mdp_actuel = value
