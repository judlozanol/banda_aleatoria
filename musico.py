from instrumento import Instrumento
class Musico():
    def __init__(self):
        self.instrumento=Instrumento
    
    def afinar_instrumento(self):
        self.instrumento.afinar()

    def tocar_instrumento(self):
        self.instrumento.tocar()

        