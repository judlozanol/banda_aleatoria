from instrumento import Instrumento
from instrumentos import *
import random
class Musico():
    def __init__(self):
        self.instrumento=Instrumento
    def asignar_instrumento(self):
        instrumentos=[Flauta(),Charrasca(), Guitarra(), Clarinete(), Trompeta(), Tuba(), Violonchelo(), Fagot(), Maracas(), Claves(), Redoblante(), Tambor()]
        self.instrumento=random.choice(instrumentos)
    def afinar_instrumento(self):
        return self.instrumento.afinar()
    def tocar_instrumento(self):
        return self.instrumento.tocar()
