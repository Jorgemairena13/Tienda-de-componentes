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
titulo =  r"""[bright_blue]
██████╗ ██████╗ ███╗   ███╗██████╗  ██████╗ ███╗   ██╗███████╗███╗   ██╗████████╗███████╗███████╗██████╗ ██████╗  ██████╗ 
██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔═══██╗████╗  ██║██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔═══██╗
██║     ██║   ██║██╔████╔██║██████╔╝██║   ██║██╔██╗ ██║█████╗  ██╔██╗ ██║   ██║   █████╗  ███████╗██████╔╝██████╔╝██║   ██║
██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║   ██║██║╚██╗██║██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ╚════██║██╔═══╝ ██╔══██╗██║   ██║
╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ╚██████╔╝██║ ╚████║███████╗██║ ╚████║   ██║   ███████╗███████║██║     ██║  ██║╚██████╔╝
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ 
[/bright_blue]
"""


#Creamos el menu
menu_contenido = """
[bold cyan]
                                1. 👥 Gestión de Clientes

                                                2. 📦 Gestión de Productos

                                3. 💰 Gestión de Ventas

                                                4. 🧾 Facturación

                                5. 🚪 Salir
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


        🔍  [yellow]Opcion 3 - Ver datos cliente[/yellow]


        📋  Opcion 4 - Ver lista clientes 
        

        🚪  [magenta]Opcion 5 - Salir[/magenta]
        [/bold cyan]
[bold red]
        Elige una opcion: 
[/bold red]    

"""

#Menu de la opcion 2
menu_opcion_2 = """
[bold cyan]
🛒  Opción 1 - Añadir producto


🗑️  Opción 2 - Eliminar producto


📋  Opción 3 - Lista de todos los productos


🚪  Opción 4 - Salir
[/bold cyan]

[bold red]
Elige una opción:
[/bold red]

"""

#Menu de la opcion 3
menu_opcion_3 = """
[bold cyan]
        Opción 1 - Registrar nueva venta

        Opción 2 - Eliminar venta

        Opción 3 - Ver lista de ventas
    
        Opción 4 - Salir
[/bold cyan]
[bold red]
        Elige una opción: 
[/bold red]    
"""

#Menu de la opcion 4
menu_opcion_4 = """
[bold cyan]
        Opción 1 - Crear factura

        Opción 2 - Ver facturas
        
        Opción 3 - Salir
[/bold cyan]
[bold red]
        Elige una opción: 
[/bold red]    
"""


#Aqui le aplicamos las propiedades al menu
menu_principal = Panel(
    Align.center(menu_combinado),
    border_style="blue"
)

#Propiedades para el menu de la opcion 1
menu_panel1 = Panel(
    Align.center(menu_opcion_1),
    border_style="blue",
    title="Gestion de clientes"
    )
#Propiedades para el menu de la opcion 2
menu_panel2 = Panel(
    Align.center(menu_opcion_2),
    border_style="blue",
    title="Gestion de productos"
    )
#Propiedades para el menu de la opcion 3
menu_panel3 = Panel(
    Align.center(menu_opcion_3),
    border_style="blue",
    title="Gestion de productos"
    )
#Propuedades del menu 4
menu_panel4 = Panel(
    Align.center(menu_opcion_4),
    border_style="blue",
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
        "telefono": "648721495",
        "email": "jorge@ejemplo.com" 
}
}

#Diccionario para ir añadiendo los articulos 
articulos = {
    "Procesadores": {
        "AMD Ryzen 5 5600X": {"precio": 299, "núcleos": 6, "frecuencia": "3.7 GHz", "stock": 50},
        "Intel Core i7-11700K": {"precio": 399, "núcleos": 8, "frecuencia": "3.6 GHz", "stock": 30},
        "AMD Ryzen 9 5950X": {"precio": 799, "núcleos": 16, "frecuencia": "3.4 GHz", "stock": 20}
    },
    "Tarjetas gráficas": {
        "NVIDIA GeForce RTX 3070": {"precio": 599, "VRAM": "8 GB", "tipo_memoria": "GDDR6", "stock": 25},
        "AMD Radeon RX 6800 XT": {"precio": 649, "VRAM": "16 GB", "tipo_memoria": "GDDR6", "stock": 15},
        "NVIDIA GeForce RTX 3080": {"precio": 699, "VRAM": "10 GB", "tipo_memoria": "GDDR6X", "stock": 10}
    },
    "Memorias RAM": {
        "Corsair Vengeance LPX 16GB": {"precio": 89, "capacidad": "16 GB", "velocidad": "3200 MHz", "stock": 100},
        "G.Skill Ripjaws V 32GB": {"precio": 159, "capacidad": "32 GB", "velocidad": "3600 MHz", "stock": 75},
        "Crucial Ballistix 64GB": {"precio": 329, "capacidad": "64 GB", "velocidad": "3200 MHz", "stock": 40}
    },
    "Almacenamiento": {
        "Samsung 970 EVO Plus 1TB": {"precio": 179, "tipo": "SSD NVMe", "capacidad": "1 TB", "stock": 60},
        "Western Digital Blue 2TB": {"precio": 59, "tipo": "HDD", "capacidad": "2 TB", "stock": 120},
        "Crucial MX500 500GB": {"precio": 69, "tipo": "SSD SATA", "capacidad": "500 GB", "stock": 80}
    },
    "Placas base": {
        "ASUS ROG Strix B550-F": {"precio": 189, "socket": "AM4", "formato": "ATX", "stock": 40},
        "MSI MPG Z590 Gaming Edge": {"precio": 229, "socket": "LGA1200", "formato": "ATX", "stock": 35},
        "Gigabyte X570 AORUS Elite": {"precio": 209, "socket": "AM4", "formato": "ATX", "stock": 30}
    },
    "Fuentes de alimentación": {
        "Corsair RM750x": {"precio": 129, "potencia": "750W", "certificación": "80+ Gold", "stock": 50},
        "EVGA SuperNOVA 850 G5": {"precio": 149, "potencia": "850W", "certificación": "80+ Gold", "stock": 40},
        "Seasonic Focus GX-1000": {"precio": 199, "potencia": "1000W", "certificación": "80+ Gold", "stock": 25}
    }
}


#Diccionario para ir añadiendo las ventas 
ventas = {
    1: {
        "cliente": "Jorge ",
        "categoria": "Procesadores",
        "producto": "AMD Ryzen 5 5600X",
        "cantidad": 1,
        "precio_unitario": 299,
        "total": 299
    }
   
}

facturas = {
     
    
}



texto_usuario = None

#Cargar barra de principio
progress = Progress(
    TextColumn("[bold blue]{task.description}"),
    BarColumn(bar_width=None, complete_style="bright_blue", pulse_style="white"),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    SpinnerColumn("dots"),
    transient=True  # Desaparece al terminar
)

progress.start()  # Iniciar el progreso
tarea = progress.add_task("Progreso", total=100)

#Bucle que itere para que valla avanzando la barra
for i in range(60):
    time.sleep(0.05)  # Simula una tarea en proceso
    progress.update(tarea, advance=2)

progress.stop()  # Detener el progreso
prompt('Tienda cargada correctamente presiona enter...', style= style)
system('cls')



while texto_usuario !=5:
#Sacamos por la terminal
    console.print(menu_principal)

    texto_usuario = prompt('', style=style)
    system("cls")

    if texto_usuario.isdigit():
        texto_usuario = int(texto_usuario)
        if texto_usuario == 1:
            while True:

                console.print(menu_panel1)
                opcion = prompt('', style=style)
                #Comprobamos que es un numero
                if opcion.isdigit(): 
                    opcion = int(opcion) #Convertimos a digito 

                    if opcion == 1:
                        # Añadir cliente
                        console.log('Introduzca NIF: ', style='yellow')
                        nif = prompt('', style=style)

                        if nif in clientes:
                            console.print(
                                Panel(
                                    "[yellow]✗ Error: El cliente ya existe[/]",
                                    title="Error", 
                                    border_style="yellow",
                                    subtitle=f"NIF duplicado: {nif}"
                                ))
                            prompt('Enter para continuar', style= style)
                            break

                        if len(nif) == 9 and nif[:8].isdigit() and nif[8].isalpha():

                            nombre = prompt("Introduzca nombre: ",style=style)

                            telefono = prompt("Introduzca su telefono: ",style=style)


                            if telefono.isdigit and len(telefono) == 9:
                                telefono = int(telefono)
                            else:
                                console.print(Panel(
                                "[red] X Formato incorrecto Ejemplo 676123456[/] ",
                                title="Incorrecto",
                                border_style= 'red',
                                
                                ))
                                continue

                            email = prompt('Introduce tu email:', style=style)

                            
                            if "@" and "." in email:
                                pass
                            else:
                                console.print(Panel(
                                "[red] X Formato incorrecto Ejemplo Jorge@ejemplo.com",
                                title="Incorrecto",
                                border_style= 'red',
                                
                                ))
                                continue


                            direcion = prompt("Dirección: ", style=style)

                            clientes[nif] = {
                                "nombre": nombre,
                                "direccion": direcion,
                                "telefono": telefono,
                                "email": email
                            }

                            console.print(
                            Panel(
                                "[bold green]✓ Cliente añadido correctamente[/]",
                                title="Éxito", 
                                border_style="green",
                                subtitle=f"NIF: {nif}"))
                        else:
                            console.print(
                                Panel(
                                "[red] X Formato incorrecto Ejemplo 12345678A[/] ",
                                title="Incorrecto",
                                border_style= 'red',
                                
                                ))
    



                    elif opcion == 2:
                        # Eliminar cliente
                        nif = prompt('Introduzca NIF del cliente a eliminar:\n',  style=style)
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
                            console.print("Cliente no encontrado",style=' bold yellow')
                        
                    #Mostar los clientes en una tabla
                    elif opcion == 4:
                        #Creamos la tabla
                        system('cls')
                        tabla = Table(
                            title="[blink]📋 Lista de Clientes[/]",
                            header_style="bold bright_cyan",
                            row_styles=["dim", ""],
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
                        str(nif),                     # Convierte nif a string
                        datos['nombre'],     # Accede al nombre del diccionario
                        datos['telefono'],     # Accede al nombre del diccionario
                        datos["direccion"] ,   # Acceder a la dirrecion
                        datos["email"]      # Acceder al email

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
                        console.print("[bold cyan]Categorías disponibles:[/bold cyan]")
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

                        tabla = Table(title="Inventario de Componentes")#Creamos la tabla
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
                            console.print("[bold red]Cliente no encontrado. Por favor, verifica el ID.[/bold red]")
                            continue

                        # Mostrar lista de productos disponibles
                        console.print("[bold cyan]Categorías disponibles:[/bold cyan]")
                        tabla = Table(title="Productos Disponibles", show_header=True, border_style='bold cyan')
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
                            console.print("[bold red]Categoría no encontrada[/bold red]")
                            continue
                            
                        producto = prompt("Introduce el nombre del producto: ", style=style)  #LE pedimos el nombre del producto
                        if producto not in articulos[categoria]:
                            console.print("[bold red]Producto no encontrado[/bold red]")
                            continue

                        # Verificar stock
                        if articulos[categoria][producto]['stock'] <= 0:
                            console.print("[bold yellow]No hay stock disponible para este producto[/bold yellow]")
                            continue

                        cantidad = int(prompt("Introduce la cantidad a vender: ", style=style))
                        if cantidad > articulos[categoria][producto]['stock']:
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
                                live.update(Panel("[green]✓ Venta registrada con éxito[/]", title="Notificación"))
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
                            console.print('Incorrecto introduce un numero')

                       

                    elif opcion == 3:  # Ver lista de ventas
                        system('cls')
                        if ventas:
                            paneles = []
                            for venta in list(ventas.values())[-5:]:  # Últimas 5 ventas
                                contenido = f"""
                                [bold]Cliente:[/] {venta['cliente']}
                                [bold]Producto:[/] {venta['producto']}
                                [bold]Total:[/] [green]{venta['total']}€[/]
                                """
                                paneles.append(Panel(contenido, border_style="cyan"))

                            console.print(Columns(paneles))
                        else:
                            console.print("[red]No hay ventas registradas.[/]")

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
                        # Mostrar clientes disponibles
                        console.print("[bold cyan]Clientes disponibles:[/bold cyan]")
                        for nif, datos in clientes.items():
                            console.print(f"NIF: {nif} - Nombre: {datos['nombre']}")

                        # Seleccionar cliente
                        nif_cliente = prompt("\nIntroduce el NIF del cliente: ")
                        if nif_cliente not in clientes:
                            console.print("[bold red]Cliente no encontrado[/bold red]")
                            continue

                        # Mostrar ventas del cliente
                        ventas_cliente = []
                        for id_venta, venta in ventas.items():
                            if venta['cliente'] == clientes[nif_cliente]['nombre']:
                                ventas_cliente.append((id_venta, venta))

                        if not ventas_cliente:
                            console.print("[bold yellow]No hay ventas para este cliente[/bold yellow]")
                            continue

                        # Mostrar ventas del cliente
                        console.print("\n[bold cyan]Ventas del cliente:[/bold cyan]")
                        for id_venta, venta in ventas_cliente:
                            console.print(f"ID: {id_venta} - Producto: {venta['producto']} - Total: {venta['total']}€")

                        # Crear factura
                        id_venta = int(prompt("\nIntroduce el ID de la venta a facturar: "))
                        if id_venta not in ventas:
                            console.print("[bold red]Venta no encontrada[/bold red]")
                            continue

                        # Generar número de factura 
                        num_factura = len(facturas) + 1

                        # Crear factura
                        facturas[num_factura] = {
                            'cliente': clientes[nif_cliente]['nombre'],
                            'nif': nif_cliente,
                            "producto": ventas[id_venta]["producto"],
                            'venta': ventas[id_venta],
                            'total': ventas[id_venta]['total'],
                            'iva': ventas[id_venta]['total'] * 0.21,
                            'total_con_iva': ventas[id_venta]['total'] * 1.21
                        }
                        progress = Progress(
                            TextColumn("[bold blue]Cargando factura[/]"),
                            BarColumn(),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                        )

                        progress.start()  # Iniciar el progreso
                        tarea = progress.add_task("Progreso", total=100)

                        #Bucle que itere para que valla avanzando la barra
                        for i in range(60):
                            time.sleep(0.05)  # Simula una tarea en proceso
                            progress.update(tarea, advance=2)

                        progress.stop()  # Detener el progreso
                        
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
                            total = f"[bold green]€{factura['total']:,.2f}[/]"
                            iva = f"[italic]€{factura['iva']:,.2f}[/]"
                            total_con_iva = f"[bold yellow]€{factura['total_con_iva']:,.2f}[/]"
                            
                            grid.add_row("Cliente:", factura['cliente'])
                            grid.add_row("Total:", total)
                            grid.add_row("IVA (21%):", iva)
                            grid.add_row("Producto:", ventas[id_venta]["producto"])
                            grid.add_row("[bold]Total con IVA:", total_con_iva)
                            grid.add_row("[bold]Total con IVA:", total_con_iva)
                            
                            console.print(Panel(grid, title=f"Factura #{num}"))

                    elif opcion == 3:  # Salir
                        system("cls")
                        break

                else:
                    console.print("[red]Por favor, introduce un número válido[/red]")

                prompt("\nPresiona Enter para continuar...")
                system('cls')
    
            
        #Salir del programa
        elif texto_usuario == 5:
            console.log("[bold green] Gracias por usar el programa[/bold green]")
            prompt("Enter para salir.....", style = style)
            break
   
         
    