from musico import Musico
from tkinter import PhotoImage
class Imagen:
    def __init__(self, musico:type[Musico]):
        self.direccion_memoria= musico.instrumento.imagen
        self.img= PhotoImage(file=self.direccion_memoria)