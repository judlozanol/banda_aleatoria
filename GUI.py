from tkinter import *

ventana= Tk()
ventana.title("Banda Aleatoria")
ventana.geometry("800x600")
ventana.config(bg="light green")
ventana.resizable(False, False)

titulo= Label(ventana, text="Banda Aleatoria", fg="dark green", font=("Helvetica",50))
titulo.pack(pady=25)

generar= Button(ventana, text="Generar Banda", fg="black",font=("Helvetica",20) )
generar.pack(pady=5)

instrumentos=Canvas(width=400,height=300, bg="white")
instrumentos.pack()

afinar= Button(ventana, text="Afinar Banda", fg="black",font=("Helvetica",10) )
afinar.place(x=250, y=525)
tocar= Button(ventana, text="Tocar\n Instrumentos", fg="black",font=("Helvetica",10) )
tocar.place(x=450, y=525)
ventana.mainloop()