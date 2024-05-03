import random
import string


class CustomCrypt:

    @staticmethod
    def saler_mdp(mdp: str) -> str:
        """Sale un mot de passe

        Args:
            mdp (str): Le mot de passe

        Returns:
            str: Le mot de passe salé
        """
        letters = string.ascii_lowercase
        sel = ''.join(random.choice(letters) for i in range(len(mdp)))
        print(f'sel : {sel}')
        return mdp + sel

    @staticmethod
    def generer_cle(mdp: str) -> tuple[int]:
        """Génère une clé à partir d'un mot de passe

        Args:
            mdp (str): Le mot de passe

        Returns:
            tuple[int]: La clé
        """
        liste = []
        for i in range(len(mdp)):
            liste.append(random.randint(0, 10))

        cle = tuple(liste)
        print(f'cle : {cle}')
        return cle

    @staticmethod
    def crypt(mdp: str, cle: tuple[int]) -> str:
        """Chiffre un mot de passe avec une clé

        Args:
            mdp (str): Le mot de passe
            cle (tuple[int]): La clé

        Returns:
            str: Le mot de passe chiffré
        """
        mdp_chiffre = ""
        for i in range(len(mdp)):
            code = (ord(mdp[i]) + cle[i]) % 128
            mdp_chiffre += chr(code)
            
        return mdp_chiffre
