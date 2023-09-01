class Instrumento():
    def __init__(self):
        self.nombre= str(type(self)).split(".")[1][:-2]
        self.afina= bool
    def afinar(self):
        if self.afina==False:
            return 0
        else:
            print("Afinando "+ self.nombre+"...")
    def tocar(self):
        print("Tocando "+ self.nombre+"...")

if __name__=="__main__":
    p=Instrumento()
    p.afina = True
    p.afinar()
    

    j=Instrumento()
    j.afina = False
    j.afinar()

    p.tocar()
    j.tocar()