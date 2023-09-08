from instrumento import Instrumento
class Flauta(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Flauta"
        self.imagen="lauta.gif"

class Guitarra(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Guitarra"
        self.imagen="guitarra.gif"

class Clarinete(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Clarinete"
        self.imagen="clarinete.gif"
class Trompeta(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Trompeta"
        self.imagen="ompeta.gif"
class Tuba(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Tuba"
        self.imagen="uba.gif"
class Violonchelo(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Violonchelo"
        self.imagen="iolonchelo.gif"
class Fagot(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Fagot"
        self.imagen="got.gif"
class Maracas(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Maracas"
        self.imagen="maracas.gif"
class Claves(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Claves"
        self.imagen="claves.gif"
class Redoblante(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Redoblante"
        self.imagen="edoblantes.gif"
class Tambor(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Tambor"
        self.imagen="mbor.gif"
class Charrasca(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Charrasca"
        self.imagen="charrasca.gif"