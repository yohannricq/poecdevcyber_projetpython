class Compte:
    
    def __init__(self, cle: str, sel: str, type: str, id_utilisateur: int) -> None:
        self.__cle = cle
        self.__sel = sel
        self.__type = type
        self.__id_utilisateur = id_utilisateur

    @property
    def cle(self):
        return self.__cle

    @property
    def sel(self):
        return self.__sel

    @property
    def type(self):
        return self.__type

    @property
    def id_utilisateur(self):
        return self.__id_utilisateur
