from instrumento import Instrumento
from instrumentos import *
import random
class Musico():
    def __init__(self):
        self.instrumento=Instrumento
    def asignar_instrumento(self):
        instrumentos=["Flauta", "Guitarra", "Clarinete", "Trompeta", "Tuba", "Violonchelo", "Fagot", "Maracas", "Claves", "Redoblante", "Tambor"]
        condicion=random.choice(instrumentos)
        if condicion=="Flauta":
            self.instrumento= Flauta()
        elif condicion=="Guitarra":
            self.instrumento= Guitarra()
        elif condicion=="Clarinete":
            self.instrumento= Clarinete()
        elif condicion=="Trompeta":
            self.instrumento= Trompeta()
        elif condicion=="Tuba":
            self.instrumento= Tuba()
        elif condicion=="Violonchelo":
            self.instrumento= Violonchelo()
        elif condicion=="Fagot":
            self.instrumento= Fagot()
        elif condicion=="Maracas":
            self.instrumento= Maracas()
        elif condicion=="Claves":
            self.instrumento= Claves()
        elif condicion=="Redoblante":
            self.instrumento= Redoblante()
        elif condicion=="Tambor":
            self.instrumento= Tambor()
    def afinar_instrumento(self):
        self.instrumento.afinar()
    def tocar_instrumento(self):
        self.instrumento.tocar()
