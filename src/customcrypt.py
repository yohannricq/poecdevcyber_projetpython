import random
import string


class CustomCrypt:

    __mdp_chiffre: str
    __sel : str
    __cle : str

    def __init__(self, mdp: str) -> None:
        self.__mdp = mdp
        self.__mdp_chiffre = ""
        self.__sel = ""
        self.__cle = ""

    @property
    def mdp(self):
        return self.__mdp

    @mdp.setter
    def mdp(self, value):
        self.__mdp = value

    @property
    def mdp_chiffre(self):
        return self.__mdp_chiffre

    @property
    def sel(self):
        return self.__sel

    @property
    def cle(self):
        return self.__cle


    def __saler_mdp(self) -> None:
        """Sale le mot de passe
        """
        letters = string.ascii_lowercase
        self.__sel = ''.join(random.choice(letters) for i in range(len(self.__mdp)))
        print(f'Sel : {self.__sel}')
        self.__mdp += self.__sel

    def __generer_cle(self) -> tuple:
        """Génère une clé à partir du mot de passe

        Returns:
            tuple: La clé
        """
        liste = []
        for i in range(len(self.__mdp)):
            liste.append(random.randint(0, 10))

        self.__cle = tuple(liste)
        print(f'Clé : {self.__cle}')
        return self.__cle

    def crypt(self) -> None:
        """Chiffre le mot de passe
        """
        self.__saler_mdp()
        print(f'Mdp après salage : {self.__mdp}')
        cle = self.__generer_cle()
        for i in range(len(self.__mdp)):
            char_mdp = self.__mdp[i]
            code_char = ord(char_mdp)
            entier_cle = cle[i]
            code = (code_char + entier_cle) % 128
            self.__mdp_chiffre += chr(code)
