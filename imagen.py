from tkinter import PhotoImage
from tkinter import Label
from tkinter import Canvas
from musico import *
class Imagen:
    def __init__(self, x1, y1, musico: type[Musico]):
        self.direccion_imagen= musico.instrumento.imagen
        self.x=x1
        self.y=y1
    def asignar_imagen(self,ventana: type[Canvas]):
        self.img= PhotoImage(file=self.direccion_imagen)
        self.lbl_img= Label(ventana, image=self.img)
        self.lbl_img.place(x=self.x,y=self.y)