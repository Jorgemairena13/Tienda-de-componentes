#Importamos modulos
from rich import print 
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from os import system
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress, BarColumn, TextColumn, SpinnerColumn
from rich.live import Live
import time
system('cls')
console = Console()


#Creamos el titulo
titulo =  r"""[#979a9a]
 ██████╗ ██████╗ ███╗   ███╗██████╗  ██████╗ ███╗   ██╗███████╗███╗   ██╗████████╗███████╗███████╗
██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔═══██╗████╗  ██║██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔════╝
██║     ██║   ██║██╔████╔██║██████╔╝██║   ██║██╔██╗ ██║█████╗  ██╔██╗ ██║   ██║   █████╗  ███████╗
██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║   ██║██║╚██╗██║██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ╚════██║
╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ╚██████╔╝██║ ╚████║███████╗██║ ╚████║   ██║   ███████╗███████║
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝

 
                                    ██████╗ ██████╗  ██████╗ 
                                    ██╔══██╗██╔══██╗██╔═══██╗
                                    ██████╔╝██████╔╝██║   ██║
                                    ██╔═══╝ ██╔══██╗██║   ██║
                                    ██║     ██║  ██║╚██████╔╝
                                    ╚═╝     ╚═╝  ╚═╝ ╚═════╝


"""


#Creamos el menu
menu_contenido = """
[bold cyan]
                                    [#45f808]  1. 👥 Gestión de Clientes [/]


                                    [#f89208]  2. 📦 Gestión de Productos [/]


                                    [#f8f408]  3. 💰 Gestión de Ventas [/]


                                    [#00f9db]  4. 🧾 Facturación [/]


                                    [magenta]  5. 🚪 Salir [/]
[/bold cyan]
[bold red]     
                                    Elige una opcion:  
[/bold red]    
                            
"""

#Combinamos el menu y el titulo
menu_combinado = f"{titulo}\n\n{menu_contenido}"


#Aqui vamos a hacer los menus de las diferentes opciones

#Menu de la opcion 1
menu_opcion_1 = """
 [bold cyan]
👤  [green]Opcion 1 - Añadir cliente[/green]


🗑️  [red]Opcion 2 - Eliminar cliente[/red]

🔍  [#2BD0F9]Opcion 3 - Ver datos cliente[/]


📋  [#f8f408]Opcion 4 - Ver lista clientes [/]


🚪  [magenta]Opcion 5 - Salir[/magenta]
[/bold cyan]
[bold red]
Elige una opcion: 
[/bold red]    

"""

#Menu de la opcion 2
menu_opcion_2 = """


[green]🛒  Opción 1 - Añadir producto[/]


[red]🗑️  Opción 2 - Eliminar producto[/]

[#f8f408]📋  Opción 3 - Lista de todos los productos[/]


[magenta]🚪  Opción 4 - Salir[/]



[bold red]Elige una opción:[/]


"""

#Menu de la opcion 3
menu_opcion_3 = """


[green]💸  Opción 1 - Registrar nueva venta[/]


[red]🗑️  Opción 2 - Eliminar venta[/]

[#f8f408]📋  Opción 3 - Ver lista de ventas[/]

[magenta]
🚪  Opción 4 - Salir[/]

[bold red]
Elige una opción: 
[/bold red]    
"""

#Menu de la opcion 4
menu_opcion_4 = """


[green]🖨️  Opción 1 - Crear factura[/]

[#f8f408]🏦  Opción 2 - Ver facturas[/]


[magenta]🚪  Opción 3 - Salir[/]



[bold red]Elige una opción:[/]
    
"""


#Aqui le aplicamos las propiedades al menu

menu_principal = Panel(
    Align.center(menu_combinado),
    border_style="#6fefce"
)

#Propiedades para el menu de la opcion 1
menu_panel1 = Panel(
    Align.center(menu_opcion_1),
    border_style="#6fefce",
    title="Gestion de clientes"
    )
#Propiedades para el menu de la opcion 2
menu_panel2 = Panel(
    Align.center(menu_opcion_2),
    border_style="#6fefce",
    title="Gestion de productos"
    )
#Propiedades para el menu de la opcion 3
menu_panel3 = Panel(
    Align.center(menu_opcion_3),
    border_style="#6fefce",
    title="Gestion de ventas"
    )
#Propuedades del menu 4
menu_panel4 = Panel(
    Align.center(menu_opcion_4),
    border_style="#6fefce",
    title="Gestión de Facturación"
)


#Estilo para los prompt
style = Style.from_dict({
    'prompt': 'bold orange',  
    '': 'cyan bold',
})


#Diccionario para ir añadiendo los clientes con sus datos
clientes = {  
"20": {  # NIF como clave principal (letra mayúscula)
        "nombre": "Jorge",  
        "direccion": "Calle Falsa 123, Mairena , Granada",
        "telefono": 648721495,
        "email": "jorge@ejemplo.com" 
}
}

#Diccionario para ir añadiendo los articulos 
articulos = {
    "Procesadores": {
        "AMD Ryzen 5": {"precio": 299, "núcleos": 6,  "stock": 50},
        "Intel Core i7": {"precio": 399, "núcleos": 8,  "stock": 30},
        "AMD Ryzen 9": {"precio": 799, "núcleos": 16,  "stock": 20}
    },
    "Tarjetas graficas": {
        "NVIDIA GeForce RTX 3070": {"precio": 599, "VRAM": "8 GB",  "stock": 25},
        "AMD Radeon RX 6800 XT": {"precio": 649, "VRAM": "16 GB", "stock": 15},
        "NVIDIA GeForce RTX 3080": {"precio": 699, "VRAM": "10 GB","stock": 10}
    },
    "Memoria ram": {
        "Corsair": {"precio": 89, "capacidad": "16 GB",  "stock": 100},
        "G.Skill": {"precio": 159, "capacidad": "32 GB",  "stock": 75},
        "Crucial": {"precio": 329, "capacidad": "64 GB",  "stock": 40}
    },
    "Almacenamiento": {
        "Samsung": {"precio": 179, "tipo": "SSD NVMe", "capacidad": "1 TB", "stock": 60},
        "Western": {"precio": 59, "tipo": "HDD", "capacidad": "2 TB", "stock": 120},
        "Crucial": {"precio": 69, "tipo": "SSD SATA", "capacidad": "500 GB", "stock": 80}
    },
    "Placas base": {
        "ASUS": {"precio": 189, "socket": "AM4",  "stock": 40},
        "MSI": {"precio": 229, "socket": "LGA1200",  "stock": 35},
        "Gigabyte": {"precio": 209, "socket": "AM4",  "stock": 30}
    },
    "Fuentes de alimentación": {
        "Corsair": {"precio": 129, "potencia": "750W","stock": 50},
        "EVGA ": {"precio": 149, "potencia": "850W", "stock": 40},
        "Seasonic": {"precio": 199, "potencia": "1000W","stock": 25}
    }
}


#Diccionario para ir añadiendo las ventas 
ventas = {
    1: {
        "cliente": "Jorge ",
        "categoria": "Procesadores",
        "producto": "AMD Ryzen 5",
        "cantidad": 1,
        "precio_unitario": 299,
        "total": 299
    }
   
}

facturas = {
    1: {
        "cliente": "Jorge",
        "nif": "20",
        "productos": [
            {"nombre": "AMD Ryzen 5 5600X", "cantidad": 1, "precio_unitario": 299, "total": 299},
            {"nombre": "NVIDIA GeForce RTX 3070", "cantidad": 2, "precio_unitario": 599, "total": 1198}
        ],
        "subtotal": 1497,
        "iva": 314.37,
        "total_con_iva": 1811.37
    }
}



texto_usuario = None

#Cargar barra de principio
progress = Progress(
    TextColumn("[bold blue]{task.description}"),
    BarColumn(bar_width=100, complete_style="bright_cyan", pulse_style="red"),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    SpinnerColumn("bouncingBall", style= "red", speed=2.0),
    transient=True  # Desaparece al terminar
)

progress.start()  # Iniciar el progreso
tarea = progress.add_task("Progreso", total=100)

#Bucle que itere para que valla avanzando la barra
for i in range(60):
    time.sleep(0.05)  # Simula una tarea en proceso
    progress.update(tarea, advance=2)

progress.stop()  # Detener el progreso
prompt('Poner pantalla completa para mejor visualizacion\nTienda cargada correctamente presiona enter...', style= style)
system('cls')



while texto_usuario !=5:

    
    #Mostramos el menu principal
    console.print(menu_principal)
    #Le pedimos al usario que opcion quiere
    texto_usuario = prompt('', style=style)
    system("cls")

    #Comprobamos que se un numero
    if texto_usuario.isdigit():
        texto_usuario = int(texto_usuario)#Le cambiamos el tipo
        #Opcion 1
        if texto_usuario == 1:
            #Bucle de la opcion 1
            while True:
                #Le mostramos el menu
                console.print(menu_panel1)

                opcion = prompt('', style=style)#le pedimos que nos de una opcion
                #Comprobamos que es un numero
                if opcion.isdigit(): 
                    opcion = int(opcion) #Convertimos a digito 

                    if opcion == 1:
                        # Añadir cliente
                        console.log('Introduzca NIF: ', style='yellow')
                        nif = prompt('', style=style).strip()

                        if nif == "": #Comprobamos que el dni no este vacio
                            system("cls")
                            console.print(Panel(
                                "[red] ❌ No has introducido nada[/] ",
                                title="Dato vacio",
                                border_style= 'red',
                                width=30,
                            
                                ),justify="center")
                            continue 
                            
                        
                        #Comprobamos que el cliente no este registrado
                        if nif in clientes :
                            console.print(
                                Panel(
                                    "[yellow]❌ Error: El cliente ya existe[/]",
                                    title="Error", 
                                    border_style="yellow",
                                    subtitle=f"NIF duplicado: {nif}",
                                    width=30
                                ),justify="center")
                            prompt('Enter para continuar', style= style)
                            break

                        if len(nif) == 9 and nif[:8].isdigit() and nif[8].isalpha():

                            nombre = prompt("Introduzca nombre: ",style=style).strip()

                            if nombre == "":
                                system("cls")
                                console.print(Panel(
                                "[red] ❌ No has introducido nada[/] ",
                                title="Dato vacio",
                                border_style= 'red',
                                width=30,
                            
                                ),justify="center")
                                continue 

                            telefono = prompt("Introduzca su telefono: ",style=style).strip()

                            if telefono == "":
                                system("cls")
                                console.print(Panel(
                                "[red] ❌ No has introducido nada[/] ",
                                title="Dato vacio",
                                border_style= 'red',
                                width=30,
                            
                                ),justify="center")
                                continue 


                            if telefono.isdigit() and len(telefono) == 9:
                                telefono = int(telefono)
                            else:
                                system("cls")
                                console.print(Panel(
                                "[red] ❌ Formato incorrecto Ejemplo 676123456[/] ",
                                title="Incorrecto",
                                border_style= 'red',
                                ))
                                continue

                            email = prompt('Introduce tu email:', style=style)

                            if email == "":
                                system("cls")
                                console.print(Panel(
                                "[red] ❌ No has introducido nada[/] ",
                                title="Dato vacio",
                                border_style= 'red',
                                width=30,
                            
                                ),justify="center")
                                continue 
                            
                            if "@" and "." in email:
                                pass
                            else:
                                system("cls")
                                console.print(Panel(
                                "[red] ❌ Formato incorrecto Ejemplo Jorge@ejemplo.com",
                                title="Incorrecto",
                                border_style= 'red',
                                
                                ))
                                continue


                            direcion = prompt("Dirección: ", style=style).strip()
                            if direcion == "":
                                system("cls")
                                console.print(Panel(
                                "[red] ❌ No has introducido nada[/] ",
                                title="Dato vacio",
                                border_style= 'red',
                                width=30,
                            
                                ),justify="center")
                                continue 

                            clientes[nif] = {
                                "nombre": nombre,
                                "direccion": direcion,
                                "telefono": telefono,
                                "email": email
                            }
                            system("cls")
                            console.print(
                            Panel(
                                "[bold green]✅ Cliente añadido correctamente[/]", 
                                border_style="green",
                                width=40,
                                subtitle=f"NIF: {nif}"),justify="center")
                        else:
                            system("cls")
                            console.print(
                                Panel(
                                "[red] ❌ Formato incorrecto Ejemplo 12345678A[/] ",
                                title="Incorrecto",
                                border_style= 'red',
                                width=30,
                                ),justify="center")
    



                    elif opcion == 2:
                        # Eliminar cliente
                        nif = prompt('Introduzca NIF del cliente a eliminar:\n',  style=style).strip()

                        #Verificar que no este vacio
                        if nif == "":
                            system("cls")
                            console.print(Panel(
                                "[red] ❌ No has introducido nada[/] ",
                                title="Dato vacio",
                                border_style= 'red',
                                width=30,
                            
                                ),justify="center")
                            continue 

                        #Verificar que este en clientes
                        if nif in clientes:
                            console.log("[bold red]Cliente eliminado[/bold red]")
                            console.log(clientes[nif], style="Red")
                            del clientes[nif]
                        else:
                            console.log("[bold yellow]Cliente no encontrado[/bold yellow]")
                        

                    elif opcion == 3:
                        # Mostrar cliente concreto que quiera 
                        nif = prompt("Introduzca NIF del cliente: ", style=style) 
                        if nif in clientes:
                            console.print(clientes[nif], style='blue')
                        else:
                            console.print(Panel(
                                    "[yellow]❌ Error: El cliente no existe[/]",
                                    title="Error de busqueda", 
                                    border_style="yellow",
                                    width=30
                                ),justify="center")
                        
                    #Mostar los clientes en una tabla
                    elif opcion == 4:
                        #Creamos la tabla
                        system('cls')
                        tabla = Table(
                            title="[blink]📋 Lista de Clientes[/]",
                            header_style="bold bright_cyan",
                            border_style="bright_yellow",
                            caption=f"Total clientes: {len(clientes)}"
                        )
                        tabla.add_column("DNI", style="italic cyan", justify="left", no_wrap=True)
                        tabla.add_column("Nombre", style="#FF69B4", justify="center")
                        tabla.add_column("Teléfono", style="bold green", justify="right")
                        tabla.add_column("Dirrecion", style="bold green", justify="right")
                        tabla.add_column("Email", style="bold green", justify="center")


                        #Bucle para ver los datos de los clientes
                        for nif, datos in clientes.items():
                             tabla.add_row(
                        str(nif),                     
                        datos['nombre'],    
                        str(datos['telefono']),     
                        datos["direccion"] ,   
                        datos["email"]      

                    )
                        #Mostramos la tabla
                        console.print(tabla)
                        
                            

                    elif opcion == 5:
                        system("cls")
                        break
                else: #Mensaje por si nos da algo que no sea un numero
                    console.print("[red]No has introducido un numero. Introduce un número.[/red]")
                prompt("Presiona enter", style=style)
                system("cls")


        #Opcion 2 del menu principal
     
        elif texto_usuario == 2:
            while True:
                console.print(menu_panel2)
                opcion = prompt("", style=style)

                if opcion.isdigit():
                    opcion = int(opcion)

                    if opcion == 1:  # Añadir producto
                        # Mostrar categorías disponibles
                        console.print("[bold cyan]Categorías disponibles:[/]")
                        for categoria in articulos.keys():
                            console.print(f"- {categoria}")
                        
                        categoria = prompt("Introduce la categoría del producto: ", style=style)
                        if categoria not in articulos:
                            articulos[categoria] = {}
                        
                        nombre_producto = prompt("Nombre del producto: ", style=style)
                        precio = int(prompt("Precio: ", style=style))
                        stock = int(prompt("Stock: ", style=style))
                        
                        # Añadir producto a la categoría
                        articulos[categoria][nombre_producto] = {
                            "precio": precio,
                            "stock": stock
                        }
                        console.print("[bold green]Producto añadido correctamente[/bold green]")

                    elif opcion == 2:  # Eliminar producto
                        # Mostrar categorías
                        console.print("[bold cyan]Categorías disponibles:[/bold cyan]")
                        for categoria in articulos.keys():
                            console.print(f"- {categoria}")
                        
                        categoria = prompt("Introduce la categoría del producto: ", style=style)
                        if categoria in articulos:
                            # Mostrar productos de la categoría
                            console.print(f"[bold cyan]Productos en {categoria}:[/bold cyan]")
                            for producto in articulos[categoria].keys():
                                console.print(f"- {producto}")
                            
                            #Le pedimos el producto a eliminar
                            producto = prompt("Nombre del producto a eliminar: ", style=style)

                            if producto in articulos[categoria]: #Comprobamos que la categoria este
                                del articulos[categoria][producto] #Eliminamos el producto
                                console.print("[bold green]Producto eliminado correctamente[/bold green]")
                            else:
                                console.print("[bold red]Producto no encontrado[/bold red]")
                        else:
                            console.print("[bold red]Categoría no encontrada[/bold red]")


                    elif opcion == 3:  # Ver lista de productos

                        tabla = Table(title="[blink]📋 Lista de Componentes[/]",#Creamos la tabla
                            header_style="bold bright_cyan",
                            border_style="bright_yellow",
                            caption=f"Total articulos: {len(articulos)}")


                        #Le añadimso las columanas a la tabla
                        tabla.add_column("Categoría", style="cyan", justify="center")
                        tabla.add_column("Producto", style="magenta", justify="center")
                        tabla.add_column("Precio (€)", style="green", justify="center")
                        tabla.add_column("Stock", style="yellow", justify="center")
                        tabla.add_column("Detalles", style="blue", justify="center")

                        for categoria, productos in articulos.items():
                            for producto, datos in productos.items():
                                # Crear string de detalles
                                detalles = []
                                for key, value in datos.items():
                                    if key not in ['precio', 'stock']:
                                        detalles.append(f"{key}: {value}")
                                detalles_str = ", ".join(detalles)

                                tabla.add_row(
                                    categoria,
                                    producto,
                                    f"{datos['precio']}€",
                                    str(datos.get('stock', '-')),
                                    detalles_str
                                )
                        system('cls')
                        console.print(tabla)

                    elif opcion == 4:  # Salir
                        system("cls")
                        break

                else:
                    console.print("[bold red]Por favor introduce un número[/bold red]")

                prompt("Presiona enter", style=style)
                system("cls")
        

        #Seccion de ventas
        elif texto_usuario == 3:
            
            n_venta = 1  # Contador para las ventas

            while True:
                
                console.print(menu_panel3)  # Mostrar el menú de ventas
                opcion = prompt("", style=style)

                if opcion.isdigit():  # Validar que la entrada sea un número
                    opcion = int(opcion)

                    if opcion == 1:  # Registrar nueva venta
                        # Validar cliente
                        id_cliente = prompt("Introduce el ID del cliente: ", style=style)

                        if id_cliente not in clientes:
                            system("cls")
                            console.print("[bold red]Cliente no encontrado. Por favor, verifica el ID.[/bold red]")
                            continue

                        # Mostrar lista de productos disponibles
                        console.print("[bold cyan]Categorías disponibles:[/bold cyan]")
                        tabla = Table(title="[[blink]]Productos Disponibles[/]", show_header=True, border_style='bold cyan')
                        tabla.add_column("Categoría", style="cyan")
                        tabla.add_column("Producto", style="magenta")
                        tabla.add_column("Precio", style="green")
                        tabla.add_column("Stock", style="yellow")

                        for categoria, productos in articulos.items():
                            for producto, datos in productos.items():
                                if datos.get('stock', 0) > 0:  # Solo mostrar productos con stock
                                    tabla.add_row(
                                        categoria,
                                        producto,
                                        f"{datos['precio']}€",
                                        str(datos.get('stock', '-'))
                                    )

                        console.print(tabla)

                        # Selección de producto
                        categoria = prompt("Introduce la categoría del producto: ", style=style)
                        categoria = categoria.capitalize()

                        if categoria not in articulos: #Comprueba que la categora no exista
                            system("cls")
                            console.print("[bold red]Categoría no encontrada[/bold red]")
                            continue
                            
                        producto = prompt("Introduce el nombre del producto: ", style=style)  #LE pedimos el nombre del producto
                        if producto not in articulos[categoria]:
                            system("cls")
                            console.print("[bold red]Producto no encontrado[/bold red]")
                            continue

                        # Verificar stock
                        if articulos[categoria][producto]['stock'] <= 0:
                            system("cls")
                            console.print("[bold yellow]No hay stock disponible para este producto[/bold yellow]")
                            continue

                        cantidad = int(prompt("Introduce la cantidad a vender: ", style=style))
                        if cantidad > articulos[categoria][producto]['stock']:
                            system("cls")
                            console.print(f"[bold yellow]Stock insuficiente. Solo hay disponible: {articulos[categoria][producto]['stock']}[/bold yellow]")
                            continue

                        # Registrar venta
                        ventas[n_venta] = {
                            "cliente": clientes[id_cliente]["nombre"],
                            "categoria": categoria,
                            "producto": producto,
                            "cantidad": cantidad,
                            "precio_unitario": articulos[categoria][producto]["precio"],
                            "total": cantidad * articulos[categoria][producto]["precio"]
                        }

                        # Actualizar stock
                        articulos[categoria][producto]["stock"] -= cantidad

                        with Live(console=console, refresh_per_second=4) as live:
                            for i in range(3):
                                live.update(Panel("[green]✅ Venta registrada con éxito[/]", title="Venta",width=30))
                                time.sleep(0.3)
                        n_venta += 1

                    elif opcion == 2:  # Eliminar venta
                        id_venta = prompt("Introduce el número de la venta a eliminar: ", style=style)
                        
                        if id_venta.isdigit():

                            id_venta = int(id_venta)
                            if id_venta in ventas:
                                venta = ventas[id_venta]
                            
                                articulos[venta["categoria"]][venta["producto"]]["stock"] += venta["cantidad"]
                                del ventas[id_venta]
                                console.print("[bold red]Venta eliminada correctamente.[/bold red]")
                            else:
                                console.print("[bold yellow]Venta no encontrada.[/bold yellow]")
                                continue
                        else:
                            console.print('[red]Incorrecto introduce un numero[/]')

                       

                    elif opcion == 3:  # Ver lista de ventas
                        system('cls')
                        if ventas:
                            paneles = []
                            for venta in list(ventas.values())[-5:]:  # Últimas 5 ventas
                                contenido = f"""
                                [bold cyan]Cliente:[/] {venta['cliente']}
                                [bold cyan]Producto:[/] {venta['producto']}
                                [bold cyan]Total:[/] [green]{venta['total']}€[/]
                                """
                                paneles.append(Panel(contenido, border_style="cyan"))

                            console.print(Columns(paneles))
                        else:
                            console.print("[#f9ec00 ]No hay ventas registradas.[/]")

                    elif opcion == 4:  # Salir
                        system("cls")
                        break

                else:
                    console.print("[bold red]Introduce un número válido.[/bold red]")
                prompt("Presiona Enter para continuar...", style=style)
                system("cls")


        


        #Seccion de facturacion
        elif texto_usuario == 4:
            while True:
                console.print(menu_panel4)
                opcion = prompt('', style=style)
                system('cls')

                if opcion.isdigit():
                    opcion = int(opcion)

                    if opcion == 1:  # Crear factura
                       # Proceso de creación de factura
 
                        # Mostrar clientes disponibles
                        console.print("[bold cyan]Clientes disponibles:[/bold cyan]")
                        for nif, datos in clientes.items():
                            console.print(f"[#68e5f6]NIF: {nif} - Nombre: {datos['nombre']}[]")
                        
                        # Seleccionar cliente
                        nif_cliente = prompt("\nIntroduce el NIF del cliente: ").strip()
                        if nif_cliente not in clientes:
                            console.print("[bold red]Cliente no encontrado[/bold red]")
                            continue

                        # Filtrar ventas del cliente
                        ventas_cliente = []
                        for id_venta, venta in ventas.items():
                            if venta["cliente"] == clientes[nif_cliente]["nombre"]:
                                ventas_cliente.append((id_venta, venta))
                        
                        if not ventas_cliente:
                            console.print("[bold yellow]No hay ventas para este cliente[/bold yellow]")
                            continue

                        # Mostrar ventas del cliente
                        console.print("\n[bold cyan]Ventas del cliente:[/bold cyan]")
                        for id_venta, venta in ventas_cliente:
                            console.print(f"[bold#72f900 ]ID: {id_venta} - Producto: {venta['producto']} - Total: {venta['total']}€[/]")

                        # Inicializar la factura
                        ventas_factura = []
                        subtotal = 0

                        while True:
                            # Seleccionar venta
                            id_venta = prompt("\nIntroduce el ID de la venta a añadir (o 'fin' para terminar): ").strip()
                            if id_venta.lower() == "fin":
                                break

                            # Verificar que la venta exista
                            if int(id_venta) not in ventas:
                                console.print("[bold red]Venta no encontrada[/bold red]")
                                continue

                            venta_seleccionada = ventas[int(id_venta)]
                            if venta_seleccionada["cliente"] != clientes[nif_cliente]["nombre"]:
                                console.print("[bold red]La venta no pertenece al cliente seleccionado[/bold red]")
                                continue

                            # Añadir venta a la factura
                            ventas_factura.append({
                                "producto": venta_seleccionada["producto"],
                                "cantidad": venta_seleccionada["cantidad"],
                                "precio_unitario": venta_seleccionada["precio_unitario"],
                                "total": venta_seleccionada["total"]
                            })
                            subtotal += venta_seleccionada["total"]

                            console.print(f"[bold green]Venta '{venta_seleccionada['producto']}' añadida a la factura[/bold green]")

                        # Calcular IVA y total con IVA
                        iva = subtotal * 0.21
                        total_con_iva = subtotal + iva

                        # Guardar la factura
                        num_factura = len(facturas) + 1
                        facturas[num_factura] = {
                            "cliente": clientes[nif_cliente]["nombre"],
                            "nif": nif_cliente,
                            "ventas": ventas_factura,
                            "subtotal": subtotal,
                            "iva": iva,
                            "total_con_iva": total_con_iva
                        }

                        console.print(f"[bold green]Factura {num_factura} creada correctamente[/bold green]")
                                            

                    elif opcion == 2:  # Ver facturas
                        if not facturas:
                            console.print("[bold yellow]No hay facturas registradas[/bold yellow]")
                            continue

                        # Crear tabla de facturas
                        tabla = Table(title="Facturas")
                        tabla.add_column("Nº Factura", style="cyan")
                        tabla.add_column("Cliente", style="magenta")
                        tabla.add_column("Producto", style="yellow")
                        tabla.add_column("Subtotal", style="green")
                        tabla.add_column("IVA", style="blue")
                        tabla.add_column("Total", style="red")

                        # En la sección de facturas (opción 4-2):
                        for num, factura in facturas.items():
                            grid = Table.grid(expand=True)
                            grid.add_column(style="bold cyan")
                            grid.add_column(style="magenta")
                            
                            # Formatear valores con estilo de moneda
                            subtotal = f"[bold green]€{factura['subtotal']:,.2f}[/]"
                            iva = f"[italic]€{factura['iva']:,.2f}[/]"
                            total_con_iva = f"[bold yellow]€{factura['total_con_iva']:,.2f}[/]"
                            
                            grid.add_row("Cliente:", factura['cliente'])
                            grid.add_row("Total:", subtotal)
                            grid.add_row("IVA (21%):", iva)
                            grid.add_row("Producto:", ventas[id_venta]['producto'])
                            grid.add_row("[bold]Total con IVA:", total_con_iva)
                            
                            
                            console.print(Panel(grid, title=f"Factura #{num}"))

                    elif opcion == 3:  # Salir
                        system("cls")
                        break

                else:
                    console.print("[red]Por favor, introduce un número válido[/red]")

                prompt("\nPresiona Enter para continuar...",style=style)
                system('cls')
    
            
        #Salir del programa
        elif texto_usuario == 5:
            console.log("[bold green] Gracias por usar el programa[/bold green]")
            prompt("Enter para salir.....", style = style)
            break