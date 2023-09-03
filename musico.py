from instrumento import Instrumento
from instrumentos import *
import random
class Musico():
    def __init__(self):
        self.instrumento=Instrumento
    def asignar_instrumento(self):
        instrumentos=["Flauta", "Guitarra"]
        condicion=random.choice(instrumentos)
        if condicion=="Flauta":
            self.instrumento= Flauta()
        elif condicion=="Guitarra":
            self.instrumento= Guitarra()
    def afinar_instrumento(self):
        self.instrumento.afinar()
    def tocar_instrumento(self):
        self.instrumento.tocar()
