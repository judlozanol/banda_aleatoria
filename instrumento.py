class Instrumento():
    def __init__(self):
        self.nombre= str
        self.afina= bool
        self.memoria=str
    def afinar(self):
        if self.afina==False:
            return 0
        else:
            print("Afinando "+ self.nombre+"...")
    def tocar(self):
        print("Tocando "+ self.nombre+"...")
