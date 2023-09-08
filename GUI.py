from tkinter import *
from banda import Banda
from imagen import Imagen
def generar_banda(widget: type[Canvas]):
    p=Banda()
    p.generar_musicos()
    x=10
    y=8
    for i in range(p.numero_musicos):
        img= Imagen(x, y, p.musicos[i])
        print(img.direccion_imagen)
        img.asignar_imagen(widget)
        img.place_imagen()
        y+=58
        if y>=298:
            y=8
            x+=195

ventana= Tk()
ventana.title("Banda Aleatoria")
ventana.geometry("800x600")
ventana.config(bg="light green")
ventana.resizable(False, False)

titulo= Label(ventana, text="Banda Aleatoria", fg="dark green", font=("Helvetica",50))
titulo.pack(pady=25)

instrumentos=Canvas(width=400,height=300, bg="white")
instrumentos.pack()

generar= Button(ventana, text="Generar Banda", fg="black",font=("Helvetica",20), command= lambda: generar_banda(instrumentos))
generar.pack(pady=5)


afinar= Button(ventana, text="Afinar Banda", fg="black",font=("Helvetica",10) )
afinar.place(x=250, y=525)

tocar= Button(ventana, text="Tocar\n Instrumentos", fg="black",font=("Helvetica",10) )
tocar.place(x=450, y=525)

ventana.mainloop()