from tkinter import Button, Tk

from .interface_inscription import InterfaceInscription
from .interface_connexion import InterfaceConnexion


class InterfaceAccueil(Tk):
    
    def __start_interface_connexion(self) -> None:
        
        self.__interface_connexion.mainloop()
        
    def __start_interface_inscription(self) -> None:
        
        self.__interface_inscription.mainloop()
    
    def __init__(self, interface_connexion: InterfaceConnexion, interface_inscription: InterfaceInscription) -> None:
        
        super().__init__()
        
        self.width = 300
        self.height = 300

        self.title('Accueil')
        self.geometry(f"{self.width}x{self.height}")
        
        self.__interface_connexion = interface_connexion
        self.__interface_inscription = interface_inscription
        
        button_connexion = Button(self, text="Connexion", command=self.__start_interface_connexion)
        button_connexion.place(x=10, y=10, height=20, width=100)
        
        button_inscription = Button(self, text="Inscription", command=self.__start_interface_inscription)
        button_inscription.place(x=130, y=10, height=20, width=100)