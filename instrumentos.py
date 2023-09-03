from instrumento import Instrumento
class Flauta(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Flauta"

class Guitarra(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Guitarra"

class Clarinete(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Clarinete"

class Trompeta(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Trompeta"

class Tuba(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Tuba"

class Violonchelo(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Violonchelo"

class Fagot(Instrumento):
    def __init__(self):
        self.afina=True
        self.nombre="Fagot"

class Maracas(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Maracas"

class Claves(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Claves"

class Redoblante(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Redoblante"

class Tambor(Instrumento):
    def __init__(self):
        self.afina=False
        self.nombre="Tambor"