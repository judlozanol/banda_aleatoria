from tkinter import *
from banda import Banda
from imagen import Imagen
def generar_banda(ventana):
    p=Banda()
    p.generar_musicos()
    x=8
    y=10
    for i in range(p.numero_musicos):
        img= Imagen(ventana, x, y, p.musicos[i])
        x+=58
        if x>=298:
            x=8
            y+=195

ventana= Tk()
ventana.title("Banda Aleatoria")
ventana.geometry("800x600")
ventana.config(bg="light green")
ventana.resizable(False, False)

titulo= Label(ventana, text="Banda Aleatoria", fg="dark green", font=("Helvetica",50))
titulo.pack(pady=25)

generar= Button(ventana, text="Generar Banda", fg="black",font=("Helvetica",20), command=generar_banda)
generar.pack(pady=5)

instrumentos=Canvas(width=400,height=300, bg="white")
instrumentos.pack()



afinar= Button(ventana, text="Afinar Banda", fg="black",font=("Helvetica",10) )
afinar.place(x=250, y=525)

tocar= Button(ventana, text="Tocar\n Instrumentos", fg="black",font=("Helvetica",10) )
tocar.place(x=450, y=525)

ventana.mainloop()