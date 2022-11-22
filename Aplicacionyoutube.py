from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("Descargar música youtube")
ventana.geometry("500x100")
ventana.resizable(False,False)
ventana.config(background="light blue")

datos_Entrada = ttk.Entry(ventana)
datos_Entrada.place(x=0,y=0)