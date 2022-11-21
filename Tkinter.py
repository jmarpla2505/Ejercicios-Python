from tkinter import *
from tkinter import ttk

def saludar():
    texto = campoTexto.get()
    print(texto)
    textoLabel.set(texto)


#Generar la ventana
ventana = Tk()
ventana.title("Primer Ejercicio")
ventana.geometry("300x400")
ventana.resizable(width=False,height=False)
ventana.config(background="light blue")

#Generar el lienzo para pintar componentes
frm = ttk.Frame(ventana)
frm.pack()


#Componentes Label y Button
textoLabel = StringVar()
textoLabel.set("Hola Tkinter")
labelTexto = ttk.Label(frm, textvariable=textoLabel)
labelTexto.config(background="sky blue", border=5, font=("Arial", 15))
labelTexto.pack()

#Componente cuadro de texto
campoTexto =ttk.Entry(frm)
campoTexto.pack()


ttk.Button(frm, text="Saludo", command=saludar).pack()

ttk.Button(frm, text="Salir", command=ventana.destroy).pack()






ventana.mainloop()