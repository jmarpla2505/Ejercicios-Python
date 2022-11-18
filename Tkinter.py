from tkinter import *
from tkinter import ttk

#Generar la ventana
ventana = Tk()
ventana.title("Primer Ejercicio")
ventana.geometry("300x400")
ventana.resizable(width=False,height=False)
ventana.config(background="light blue")
ventana.iconbitmap("icon.png")

#Generar el lienzo para pintar componentes
frm = ttk.Frame(ventana, ).pack()


#Componentes Label y Button
labelTexto = ttk.Label(frm, text="Hola Tkinter")
labelTexto.config(background="red", border=5, font=("Arial", 15))
labelTexto.pack()
ttk.Button(frm, text="Salir", command=ventana.destroy).pack()

ventana.mainloop()