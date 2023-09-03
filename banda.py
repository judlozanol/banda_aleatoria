from musico import Musico
import random

class Banda():
    def __init__(self):
        self.numero_musicos= random.randint(1,10)
        self.musicos =[]
    def generar_musicos(self):     
        for i in range(self.numero_musicos):
            m=Musico()
            m.asignar_instrumento()
            self.musicos.append(m)
    def afinar_instrumentos(self):
        for i in range(self.numero_musicos):
            self.musicos[i].afinar_instrumento()
    def tocar_instrumentos(self):
        for i in range(self.numero_musicos):
            self.musicos[i].tocar_instrumento()