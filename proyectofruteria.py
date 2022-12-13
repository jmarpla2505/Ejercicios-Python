import flet as ft


lista_seleccionados = []


def main(page:ft.Page):
    page.title = "Aplicación frutería"

    def dropdown_changed(e):
        ts.value = f"Elegido {dropDown_Menu.value}"
        page.update()
    def dropdown_changed2(e):
        tt.value = f"Elegido {dropDown_Menu2.value}"
        page.update()
    

    #Componente texto
    t=ft.Text(value="Bienvenido", color="green", size=30)
    page.add(t)

  
    textField_Nombre = ft.TextField(label="Nombre", hint_text="Escribe tu nombre", width= 400)
    #page.add(textField_Nombre)

    ts = ft.Text()
    dropDown_Menu = ft.Dropdown(width=400, label="Verduras y hortalizas", on_change=dropdown_changed, options=[ft.dropdown.Option("Lechuga")])
    #page.add(dropDown_Menu)
    dropDown_Menu.options.append(ft.dropdown.Option("Zanahorias"))
    dropDown_Menu.options.append(ft.dropdown.Option("Cebollas"))
    dropDown_Menu.options.append(ft.dropdown.Option("Tomates"))
    dropDown_Menu.options.append(ft.dropdown.Option("Pimientos"))
    page.add(ts)

    tt = ft.Text()
    dropDown_Menu2 = ft.Dropdown(width=400, label="Carne", on_change=dropdown_changed2, options=[ft.dropdown.Option("Ternera")])
    #page.add(dropDown_Menu)
    dropDown_Menu2.options.append(ft.dropdown.Option("Cerdo"))
    dropDown_Menu2.options.append(ft.dropdown.Option("Pollo"))
    dropDown_Menu2.options.append(ft.dropdown.Option("Cordero"))
    page.add(tt)

    slider_verdura = ft.Slider(min=0, max=1500, divisions=30, label="Cantidad: {value} g")
    slider_carne = ft.Slider(min=0, max=2000, divisions=40, label="Cantidad: {value} g")


    #Crear fila
    fila = ft.Row(controls=[textField_Nombre])
    page.add(fila)
    fila2 = ft.Row(controls = [dropDown_Menu, slider_verdura])
    page.add (fila2)
    fila3 = ft.Row(controls=[dropDown_Menu2, slider_carne])
    page.add(fila3)

    #slider_verdura = ft.Slider(min=0, max=1500, divisions=30, label="Peso: {value} g")
    #page.add(slider_verdura)

    lista_seleccionados.append(ts.value)
    lista_seleccionados.append(tt.value)
    print(lista_seleccionados)
    
   

    


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