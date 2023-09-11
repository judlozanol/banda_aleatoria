from instrumento import Instrumento
class Flauta(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Flauta"
        self.memoria="imagenes\imgflauta.png"

class Guitarra(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Guitarra"
        self.memoria="imagenes\imgguitarra.png"

class Clarinete(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Clarinete"
        self.memoria="imagenes\imgclarinete.png"
class Trompeta(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Trompeta"
        self.memoria="imagenes\imgtrompeta.png"
class Tuba(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Tuba"
        self.memoria="imagenes\imgtuba.png"
class Violonchelo(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Violonchelo"
        self.memoria="imagenes\imgviolonchelo.png"
class Fagot(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Fagot"
        self.memoria="imagenes\imgfagot.png"
class Maracas(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Maracas"
        self.memoria="imagenes\imgmaracas.png"
class Claves(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Claves"
        self.memoria="imagenes\imgclaves.png"
class Redoblante(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Redoblante"
        self.memoria="imagenes\imgredoblantes.png"
class Tambor(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Tambor"
        self.memoria="imagenes\imgtambor.png"
class Charrasca(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Charrasca"
        self.memoria="imagenes\imgcharrasca.png"