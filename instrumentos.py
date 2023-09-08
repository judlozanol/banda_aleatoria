from instrumento import Instrumento
class Flauta(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Flauta"
        self.imagen="flauta.png"

class Guitarra(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Guitarra"
        self.imagen="guitarra.png"

class Clarinete(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Clarinete"
        self.imagen="clarinete.png"
class Trompeta(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Trompeta"
        self.imagen="trompeta.png"
class Tuba(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Tuba"
        self.imagen="tuba.png"
class Violonchelo(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Violonchelo"
        self.imagen="violonchelo.png"
class Fagot(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Fagot"
        self.imagen="fagot.png"
class Maracas(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Maracas"
        self.imagen="maracas.png"
class Claves(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Claves"
        self.imagen="claves.png"
class Redoblante(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Redoblante"
        self.imagen="redoblantes.png"
class Tambor(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Tambor"
        self.imagen="tambor.png"
class Charrasca(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Charrasca"
        self.imagen="charrasca.png"