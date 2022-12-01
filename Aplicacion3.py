from tkinter import *
from tkinter import ttk
from tkinter import messagebox

Ingredientes = ""
def guardarDatos():
    Ingredientes = combo_ingredientes.get()
    combo_ingredientes.delete(0,len(Ingredientes))
    messagebox.showinfo("Usuario guardado",f"Usuario {Ingredientes} guardado correctamente")

ventana = Tk()
ventana.title("Ingredientes")
ventana.geometry("500x250")
ventana.resizable(False,False)
ventana.config(background="light blue")

combo_ingredientes = ttk.Combobox(ventana,values=["Carne","Verdura"])
label_combo = ttk.Label(ventana, text="Dime un ingrediente:")
label_combo.config(background="light blue")
combo_ingredientes.set("(Seleccione un sexo)")
combo_ingredientes.state(["readonly"])

combo_ingredientes.grid(row=5, column=1, pady=8)
label_combo.grid(row=5, column=0,pady=8)

ventana.mainloop()