class Compte:
    
    def __init__(self, cle: str, sel: str, type: str, id_utilisateur: int) -> None:
        self.__cle = cle
        self.__sel = sel
        self.__type = type
        self.__id_utilisateur = id_utilisateur

    @property
    def cle(self):
        return self.__cle

    # @cle.setter
    # def __cle(self, value):
    #     self.__cle = value

    @property
    def sel(self):
        return self.__sel

    # @sel.setter
    # def __sel(self, value):
    #     self.__sel = value

    @property
    def type(self):
        return self.__type

    # @type.setter
    # def type(self, value):
    #     self.__type = value

    @property
    def id_utilisateur(self):
        return self.__id_utilisateur

    # @id_utilisateur.setter
    # def __id_utilisateur(self, value):
    #     self.__id_utilisateur = value
