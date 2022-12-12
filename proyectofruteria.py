import flet as ft


lista_seleccionados = []


def main(page:ft.Page):
    page.title = "Aplicación frutería"

    def dropdown_changed(e):
        ts.value = f"Elegido {dropDown_Menu.value}"
        page.update()

    

    #Componente texto
    t=ft.Text(value="Bienvenido", color="green", size=30)
    page.add(t)

  
    textField_Nombre = ft.TextField(label="Nombre", hint_text="Escribe tu nombre")
    #page.add(textField_Nombre)

    ts = ft.Text()
    dropDown_Menu = ft.Dropdown(width=300, label="Verduras y hortalizas", on_change=dropdown_changed, options=[ft.dropdown.Option("Lechuga")])
    #page.add(dropDown_Menu)
    dropDown_Menu.options.append(ft.dropdown.Option("Zanahorias"))
    dropDown_Menu.options.append(ft.dropdown.Option("Cebollas"))
    dropDown_Menu.options.append(ft.dropdown.Option("Tomates"))
    dropDown_Menu.options.append(ft.dropdown.Option("Pimientos"))
    page.add(ts)

    #Crear fila
    fila = ft.Row(controls=[textField_Nombre,dropDown_Menu])
    page.add(fila)

    slider_edad = ft.Slider(min=0, max=120, divisions=120, label="Edad: {value}")
    page.add(slider_edad)

    #lista_seleccionados.append()
    


    '''''
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)

    count = 1

    for i in range(0, 60):
        lv.controls.append(ft.Text(f"Line {count}"))
        count += 1

    page.add(lv)

    for i in range(0, 60):
        time.sleep(1)
        lv.controls.append(ft.Text(f"Line {count}"))
        count += 1
        page.update()
    '''''


ft.app(target=main)
#Nombre y elementos que se lleva