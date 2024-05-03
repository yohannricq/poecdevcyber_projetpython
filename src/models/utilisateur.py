class Utilisateur:

    def __init__(self, nom: str, prenom: str, email: str, mdp_actuel: str) -> None:
        self.__nom = nom
        self.__prenom = prenom
        self.__email = email
        self.__mdp_actuel = mdp_actuel

    @property
    def nom(self):
        return self.__nom

    @property
    def prenom(self):
        return self.__prenom

    @property
    def email(self):
        return self.__email

    @property
    def mdp_actuel(self):
        return self.__mdp_actuel
