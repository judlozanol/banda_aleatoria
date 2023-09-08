from tkinter import *
from banda import Banda
from imagen import Imagen
class AppBanda:
    def __init__(self):
        self.banda = Banda()
        self.ventana= Tk()
        self.titulo= Label(self.ventana, text="Banda Aleatoria",font=("Helvetica",50), fg="dark green")
        self.canva= Canvas(width=400,height=300, bg="white")
        self.generar= Button(self.ventana, text="Generar Banda", fg="black",font=("Helvetica",20))
        self.afinar=Button(self.ventana, text="Afinar Banda", fg="black",font=("Helvetica",10) )
        self.tocar= Button(self.ventana, text="Tocar\n Instrumentos", fg="black",font=("Helvetica",10))
    def ejecutar(self):
        self.ventana.geometry("800x600")
        self.ventana.title("Banda Aleatoria")
        self.ventana.config(bg="light green")
        self.ventana.resizable(False,False)
        self.titulo.pack(pady=25)
        self.canva.pack()
        self.generar.pack(pady=5)
        self.afinar.place(x=250, y=525)
        self.tocar.place(x=450, y=525)


if __name__=="__main__":
    p=AppBanda()
    p.ejecutar()
    p.ventana.mainloop()