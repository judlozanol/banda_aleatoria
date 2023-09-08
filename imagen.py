from tkinter import PhotoImage
from tkinter import Label
from musico import *
class Imagen:
    def __init__(self, x, y, musico=Musico):
        self.musico=musico
        self.direccion_imagen= str
        self.x=x
        self.y=y
    def colocar__imagen(self):
        self.place(x=self.x,y=self.y)
    def asignar_imagen(self,ventana):
        self.direccion_imagen= self.Musico.instrumento.imagen
        self.img= PhotoImage(file=self.direccion_imagen)
        self.lbl_img= Label(ventana, image=self.img)