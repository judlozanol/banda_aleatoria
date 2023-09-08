from instrumento import Instrumento
class Flauta(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Flauta"
        self.memoria="flauta.png"

class Guitarra(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Guitarra"
        self.memoria="guitarra.png"

class Clarinete(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Clarinete"
        self.memoria="clarinete.png"
class Trompeta(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Trompeta"
        self.memoria="trompeta.png"
class Tuba(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Tuba"
        self.memoria="tuba.png"
class Violonchelo(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Violonchelo"
        self.memoria="violonchelo.png"
class Fagot(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Fagot"
        self.memoria="fagot.png"
class Maracas(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Maracas"
        self.memoria="maracas.png"
class Claves(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Claves"
        self.memoria="claves.png"
class Redoblante(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Redoblante"
        self.memoria="redoblantes.png"
class Tambor(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Tambor"
        self.memoria="tambor.png"
class Charrasca(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Charrasca"
        self.memoria="charrasca.png"