from tkinter import *
from tkinter import ttk
from tkinter import messagebox


usuario = ""
contraseña = ""
repiteC = ""
vUsuarios = []
vContraseña = []


def guardarDatos():
    usuario = datos_Usuario.get()
    contraseña= datos_Contraseña.get()
    repiteC = datos_Confirmacontr.get()
    if contraseña==repiteC:
        vUsuarios.append(usuario)
        vUsuarios.append(contraseña)
        print(usuario,contraseña)
        datos_Usuario.delete(0,len(usuario))
        datos_Contraseña.delete(0,len(contraseña))
        datos_Confirmacontr.delete(0,len(repiteC))
        messagebox.showinfo("Usuario guardado",f"Usuario {usuario} guardado correctamente")
    
    

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
datos_Contraseña = ttk.Entry(ventana,show="*")


label_Confirmacontr = ttk.Label(ventana, text="Confirma la contraseña:")
label_Confirmacontr.config(background="light blue")
datos_Confirmacontr = ttk.Entry(ventana,show="*")

boton_Guardar =ttk.Button(ventana,text="Guardar",command=guardarDatos)
boton_Salir =ttk.Button(ventana,text="Salir", command=ventana.destroy)
boton_Guardar.grid(row=5,column=0,pady=10)
boton_Salir.grid(row=5,column=1,pady=10)

#Pintar en pantalla los componentes
label_Titulo.grid(row=0,column=1,pady=5)

label_Usuario.grid(row=1,column=0)
datos_Usuario.grid(row=1,column=1,pady=10)

label_Contraseña.grid(row=2,column=0)
datos_Contraseña.grid(row=2,column=1,pady=10)


label_Confirmacontr.grid(row=4,column=0,padx=8)
datos_Confirmacontr.grid(row=4,column=1,pady=8)





ventana.mainloop()
