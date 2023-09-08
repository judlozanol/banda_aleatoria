from instrumento import Instrumento
class Flauta(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Flauta"
        self.imagen="Imagenes\lauta.png"

class Guitarra(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Guitarra"
        self.imagen="Imagenes\guitarra.png"

class Clarinete(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Clarinete"
        self.imagen="Imagenes\clarinete.png"
class Trompeta(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Trompeta"
        self.imagen="Imagenes\ompeta.png"
class Tuba(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Tuba"
        self.imagen="Imagenes\uba.png"
class Violonchelo(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Violonchelo"
        self.imagen="Imagenes\iolonchelo.png"
class Fagot(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Fagot"
        self.imagen="Imagenes\got.png"
class Maracas(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Maracas"
        self.imagen="Imagenes\maracas.png"
class Claves(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Claves"
        self.imagen="Imagenes\claves.png"
class Redoblante(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Redoblante"
        self.imagen="Imagenes\edoblantes.png"
class Tambor(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Tambor"
        self.imagen="Imagenes\mbor.png"
class Charrasca(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Charrasca"
        self.imagen="Imagenes\charrasca.png"