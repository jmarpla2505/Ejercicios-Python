from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("Login")
ventana.geometry("500x250")
ventana.resizable(False,False)
ventana.config(background="light blue")

label_Titulo = ttk.Label(ventana, text="Datos usuario")
label_Titulo.config(background="light blue")

label_Usuario = ttk.Label(ventana, text="Introduce tu usuario:")
label_Usuario.config(background="light blue")
datos_Usuario = ttk.Entry(ventana)

label_Contraseña = ttk.Label(ventana, text="Introduce tu contraseña:")
label_Contraseña.config(background="light blue")
datos_Contraseña = ttk.Entry(ventana)

label_Repiteusuario = ttk.Label(ventana, text="Repite tu usuario:")
label_Repiteusuario.config(background="light blue")
datos_Repiteusuario = ttk.Entry(ventana)

label_Confirmacontr = ttk.Label(ventana, text="Confirma la contraseña:")
label_Confirmacontr.config(background="light blue")
datos_Confirmacontr = ttk.Entry(ventana)

boton_Guardar =ttk.Button(ventana,text="Guardar")
boton_Salir =ttk.Button(ventana,text="Salir", command=ventana.destroy)
boton_Guardar.place(x=208,y=200)
boton_Salir.place (x=400,y=210)

#Pintar en pantalla los componentes
label_Titulo.grid(row=0,column=1)

label_Usuario.grid(row=1,column=0)
datos_Usuario.grid(row=1,column=1)

label_Contraseña.grid(row=2,column=0)
datos_Contraseña.grid(row=2,column=1)

label_Repiteusuario.grid(row=3,column=0)
datos_Repiteusuario.grid(row=3,column=1)

label_Confirmacontr.grid(row=4,column=0)
datos_Confirmacontr.grid(row=4,column=1)





ventana.mainloop()
