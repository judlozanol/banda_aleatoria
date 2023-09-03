from instrumento import Instrumento
class Flauta(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Flauta"
        
class Guitarra(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Guitarra"