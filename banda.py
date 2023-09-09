from musico import Musico
import random
class Banda():
    def __init__(self):
        self.numero_musicos= random.randint(1,10)
        self.musicos =[]
        self.creada =False
        self.afinada=False
    def generar_musicos(self):     
        for i in range(self.numero_musicos):
            m=Musico()
            m.asignar_instrumento()
            self.musicos.append(m)
        self.creada=True
    def afinar_instrumentos(self):
        for i in range(self.numero_musicos):
            a=self.musicos[i].afinar_instrumento()
            if a!=None:
                print(a)
    def tocar_instrumentos(self):
        for i in range(self.numero_musicos):
            print(self.musicos[i].tocar_instrumento())
