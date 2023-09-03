from musico import Musico
from flauta import Flauta
from guitarra import Guitarra
import random

class Banda():
    def __init__(self):
        self.numero_musicos= random.randint(1,10)
        self.musicos =[]
    def asignar_instrumento(self):
        instrumentos=["Flauta", "Guitarra"]
        condicion=random.choice(instrumentos)
        if condicion=="Flauta":
            self.instrumento= Flauta()
        elif condicion=="Guitarra":
            self.instrumento= Guitarra()

