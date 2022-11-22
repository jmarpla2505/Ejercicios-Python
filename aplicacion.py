from tkinter import *
from tkinter import ttk
from pytube import YouTube


def descargaCancion():
    url = datos_Entrada.get()
    youtube = YouTube(url)
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion = youtube.streams.get_audio_only()
    cancion.download()


ventana = Tk()
ventana.title("Descargar música youtube")
ventana.geometry("500x150")
ventana.resizable(False,False)
ventana.config(background="light blue")

datos_Entrada = ttk.Entry(ventana)
datos_Entrada.place(x=168,y=45)

boton_Descargar =ttk.Button(ventana,text="Descargar", command=descargaCancion)
boton_Descargar.place(x=208,y=80)


label_Titulo = ttk.Label(ventana, text="Introduce la url del video:")
label_Titulo.config(background="aquamarine")
label_Titulo.place(x=166,y=23)




ventana.mainloop()