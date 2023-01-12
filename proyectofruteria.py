import flet as ft


lista_seleccionados = []


def main(page:ft.Page):
    page.title = "Frutería"

    def dropdown_changed(e):
        ts.value = f"Elegido {dropDown_Menu.value}"
        page.update()
    def dropdown_changed2(e):
        tt.value = f"Elegido {dropDown_Menu2.value}"
        page.update()
    def guardar(e):
        lista_seleccionados.append(ts.value)
        lista_seleccionados.append(slider_verdura.value)
        lista_seleccionados.append(tt.value)
        lista_seleccionados.append(slider_carne.value)
        print(lista_seleccionados)
        #tl = ft.Text()
        #lista_seleccionados()
        #fila4 = ft.Row(controls=[tl])
        #page.add(fila4)

        #lista_seleccionados.clear()
    def imagen(e):
        img2 = ft.Image(
            src=f"https://img.freepik.com/vector-gratis/fondo-pantalla-multiples-frutas-verduras_23-2148481554.jpg?w=2000",
            width=100,
            height=100,
        fit=ft.ImageFit.CONTAIN, )
        page.add(img2)
    #Componente texto
    t=ft.Text(value="Bienvenido", color="green", size=30)
    page.add(t)

  
    textField_Nombre = ft.TextField(label="Nombre", hint_text="Escribe tu nombre", width= 400)
    #page.add(textField_Nombre)

    ts = ft.Text()
    dropDown_Menu = ft.Dropdown(width=400, label="Verduras y hortalizas", on_change=dropdown_changed, options=[ft.dropdown.Option("Lechuga")], on_focus=imagen)
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

    bt = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=guardar)
    page.add(bt)

    img = ft.Image(
        src=f"Imagenes/fruta.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    #Crear fila
    fila0 = ft.Row(controls=[img])
    page.add(fila0)
    fila = ft.Row(controls=[textField_Nombre])
    page.add(fila)
    fila2 = ft.Row(controls = [dropDown_Menu, slider_verdura])
    page.add (fila2)
    fila3 = ft.Row(controls=[dropDown_Menu2, slider_carne])
    page.add(fila3)

    #slider_verdura = ft.Slider(min=0, max=1500, divisions=30, label="Peso: {value} g")
    #page.add(slider_verdura)

    #tl = ft.Text()
    #lista_seleccionados()
    #lista_seleccionados = tl
    #fila4 = ft.Row(controls=[tl])
    #page.add(fila4)

    '''''
    images = ft.Row(expand=1, wrap=False, scroll="always")

    page.add(images)

    for i in range(0, 30):
        images.controls.append(
            ft.Image(
                src=f"https://picsum.photos/200/200?{i}",
                width=200,
                height=200,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )
    page.update()
    '''''
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


ft.app(target=main, assets_dir="recursos")