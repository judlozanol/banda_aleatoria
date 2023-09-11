class Instrumento():
    def __init__(self):
        self.nombre= str
        self.afina= bool
        self.memoria=str
    def afinar(self):
        if self.afina==False:
            return ("No se puede afinar")
        else:
            return("Afinando "+ self.nombre+"...")
    def tocar(self):
            return("Tocando "+ self.nombre+"...")
