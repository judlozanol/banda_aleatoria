from tkinter import *
from tkinter import messagebox
from banda import Banda

class AppBanda:
    def __init__(self):
        self.ventana= Tk()
        self.titulo= Label(self.ventana, text="Banda Aleatoria",font=("Helvetica",50), fg="dark green")
        self.canva= Canvas(width=400,height=300, bg="white")
        self.generar= Button(self.ventana, text="Generar Banda", fg="black",font=("Helvetica",20), command=self.colocar_labels_imagen)
        self.afinar=Button(self.ventana, text="Afinar Banda", fg="black",font=("Helvetica",10),command=self.afinar_banda)
        self.tocar= Button(self.ventana, text="Tocar\n Instrumentos", fg="black",font=("Helvetica",10),command=self.tocar_instrumentos)
        self.labels_imagen=[]
        self.labels_texto=[]
        self.banda= Banda()
    def destruir_labels(self,listalabel: type[list]):
        for i in range(len(listalabel)):
            listalabel[i].after(0, listalabel[i].destroy)
    def colocar_labels_imagen(self):
        global imagen
        global imagenes
        self.destruir_labels(self.labels_imagen)
        self.destruir_labels(self.labels_texto)
        imagenes=[]
        self.labels_imagen=[]
        banda=Banda()
        banda.generar_musicos()
        self.banda=banda
        for i in range(banda.numero_musicos):
            imagen=PhotoImage(file=banda.musicos[i].instrumento.memoria)
            imagenes.append(imagen)
        x1=10
        y1=8
        for i in range(banda.numero_musicos):
            label= Label(self.canva, image=imagenes[i])
            self.labels_imagen.append(label)
            self.labels_imagen[i].place(x=x1, y=y1)
            y1+=58
            if y1>=298:
                y1=8
                x1+=195
    def afinar_banda(self):
        if self.banda.creada==False:
            messagebox.showinfo("Afinar Banda", "Banda inexistente. Cree una banda para poder afinar")
        else:
            self.destruir_labels(self.labels_texto)
            self.labels_texto=[]
            x1=70
            y1=8
            for i in range(self.banda.numero_musicos):
                if self.banda.musicos[i].afinar_instrumento()==None:
                    label= Label(self.canva,text=" ")
                else:
                    label= Label(self.canva,text=self.banda.musicos[i].afinar_instrumento())
                self.labels_texto.append(label)
                self.labels_texto[i].place(x=x1, y=y1)
                y1+=58
                if y1>=298:
                    y1=8
                    x1=265

            self.banda.afinada=True
    def tocar_instrumentos(self):
        if self.banda.creada==False:
            messagebox.showinfo("Tocar Instrumentos", "Banda inexistente. Cree una banda y afinela para poder tocar")
        elif self.banda.afinada==False:
            messagebox.showinfo("Tocar Instrumentos", "Afine la banda antes de tocar los instrumentos")
        else:
            messagebox.showinfo("Hola", "Hola Causa")
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
    
