from tkinter import *
from banda import Banda

class AppBanda:
    def __init__(self):
        self.ventana= Tk()
        self.titulo= Label(self.ventana, text="Banda Aleatoria",font=("Helvetica",50), fg="dark green")
        self.canva= Canvas(width=400,height=300, bg="white")
        self.generar= Button(self.ventana, text="Generar Banda", fg="black",font=("Helvetica",20), command=self.colocar_labels)
        self.afinar=Button(self.ventana, text="Afinar Banda", fg="black",font=("Helvetica",10) )
        self.tocar= Button(self.ventana, text="Tocar\n Instrumentos", fg="black",font=("Helvetica",10))
    def colocar_labels(self):
        global imagen
        global imagenes
        imagenes=[]
        labels=[]
        banda=Banda()
        banda.generar_musicos()
        for i in range(banda.numero_musicos):
            imagen=PhotoImage(file=banda.musicos[i].instrumento.memoria)
            imagenes.append(imagen)
        x1=10
        y1=8
        for i in range(banda.numero_musicos):
            label= Label(self.canva, image=imagenes[i])
            labels.append(label)
            labels[i].place(x=x1, y=y1)
            y1+=58
            if y1>=298:
                y1=8
                x1+=195
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
    
