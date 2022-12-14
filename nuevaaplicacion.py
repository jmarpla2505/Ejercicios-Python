import flet as ft

def main(page:ft.Page):
    page.title = ":-)"

    def cambiarColor(e):
        t.value = textField_Nombre.value

    #Componente texto
    t=ft.Text(value="Introducción a Flet", color="red", size=20)
    page.add(t)
    #Componente boton
    bt = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=cambiarColor)
    page.add(bt)

    
    textField_Nombre = ft.TextField(label="Nombre", hint_text="Escribe tu nombre")
    #page.add(textField_Nombre)


    dropDown_Menu = ft.Dropdown(width=300, options=[ft.dropdown.Option("Opción 1")])
    #page.add(dropDown_Menu)
    dropDown_Menu.options.append(ft.dropdown.Option("Opción 2"))
    dropDown_Menu.options.append(ft.dropdown.Option("Opción 3"))
    page.update()

    #Crear fila
    fila = ft.Row(controls=[textField_Nombre,dropDown_Menu])
    page.add(fila)

    slider_edad = ft.Slider(min=0, max=120, divisions=120, label="Edad: {value}")
    page.add(slider_edad)


ft.app(target=main)
#Nombre y elementos que se lleva