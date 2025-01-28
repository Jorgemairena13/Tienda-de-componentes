#Importamos modulos
from rich import print 
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from os import system
from rich.table import Table
from datos import cargar_datos, guardar_datos
console = Console()


#Creamos el titulo
titulo = r"""[bright_blue]
     ____                                             _            ____               
    / ___|___  _ __ ___  _ __   ___  _ __   ___ _ __ | |_ ___  ___|  _ \ _ __ ___     
   | |   / _ \| '_ ` _ \| '_ \ / _ \| '_ \ / _ \ '_ \| __/ _ \/ __| |_) | '__/ _ \    
   | |__| (_) | | | | | | |_) | (_) | | | |  __/ | | | ||  __/\__ \  __/| | | (_) |   
    \____\___/|_| |_| |_| .__/ \___/|_| |_|\___|_| |_|\__\___||___/_|   |_|  \___/    
                        |_|                                                           
[/bright_blue]
                        """

#Creamos el menu
menu_contenido = """
[bold cyan]
                                Opcion 1 - Gestion clientes

                                Opcion 2 - Gestion inventario

                                Opcion 3 - Ventas

                                Opcion 4 - Facturacion

                                Opcion 5 - Salir
[/bold cyan]
[bold red]     
                                Elige una opcion:  
[/bold red]    
                            
"""

#Combinamos el menu y el titulo
menu_combinado = f"{titulo}\n\n{menu_contenido}"


#Aqui vamos a hacer los menus de las diferentes opciones
menu_opcion_1 = """
 [bold cyan]
        Opcion 1 - Añadir cliente

        Opcion 2 - Eliminar cliente

        Opcion 3 - Ver datos cliente

        Opcion 4 - Ver lista clientes 
        
        Opcion 5 - Salir[/bold cyan]
[bold red]
        Elige una opcion: 
[/bold red]    

"""
menu_opcion_2 = """
[bold cyan]
Opción 1 - Añadir producto

Opción 2 - Eliminar producto

Opción 3 - Lista de todos los productos

Opción 4 - Salir
[/bold cyan]

[bold red]
Elige una opción:
[/bold red]

"""



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


#Estilo para los prompt
style = Style.from_dict({
    'prompt': 'bold orange',  
    '': 'cyan bold',
})


#Diccionario para ir añadiendo los clientes con sus datos

clientes, articulos, ventas = cargar_datos()


#Diccionario para ir añadiendo los articulos 

texto_usuario = None

while texto_usuario !=6:
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
                            console.print('Cliente ya existente')
                            break

                        nombre = input("Introduzca nombre: ")
                        clientes[nif] = {
                            "nombre": nombre,
                            "direccion": input("Dirección: "),
                            "telefono": input("Teléfono: ")
                        }
                        print("Cliente añadido correctamente")
                        guardar_datos(clientes,articulos,ventas)

                    elif opcion == 2:
                        # Eliminar cliente
                        nif = input('Introduzca NIF del cliente a eliminar:\n')
                        if nif in clientes:
                            console.log("[bold red]Cliente eliminado[/bold red]")
                            console.log(clientes[nif], style="Red")
                            del clientes[nif]
                            guardar_datos(clientes,articulos,ventas)
                        else:
                            console.log("[bold yellow]Cliente no encontrado[/bold yellow]")
                        

                    elif opcion == 3:
                        # Mostrar cliente concreto que quiera 
                        nif = input("Introduzca NIF del cliente: ")
                        if nif in clientes:
                            print(clientes[nif])
                        else:
                            print("Cliente no encontrado")
                        
                        
                    elif opcion == 4:
                        #Creamos la tabla
                        system('cls')
                        tabla = Table(title="Clientes", expand=True, show_header=True, border_style='bold cyan')

                        #Añadimos columnas
                        tabla.add_column("DNI", style="bold cyan", justify="'right")
                        tabla.add_column("Nombre", style="magenta", justify="center")
                        tabla.add_column("Telefono", style="magenta", justify="center")
                        tabla.add_column("Dirrecion", style="magenta", justify="right")


                        #Bucle para ver los datos de los clientes
                        for nif, datos in clientes.items():
                             tabla.add_row(
                        str(nif),                     # Convierte nif a string
                        datos['nombre'],     # Accede al nombre del diccionario
                        datos['telefono'],     # Accede al nombre del diccionario
                        datos["direccion"]    # Acceder a la dirrecion

                    )
                        #Mostramos la tabla
                        console.print(tabla)
                        
                            

                    elif opcion == 5:
                        break
                else: #Mensaje por si nos da algo que no sea un numero
                    console.print("[red]No has introducido un numero. Introduce un número.[/red]")
                input("Presiona enter")
                system("cls")



        #Opcion 2 del menu principal
        elif texto_usuario == 2:
            #Creamos el bucle para que este siempre abierta 
            while True:
                console.print(menu_panel2) #Mostramos menu
                opcion = prompt("", style=style)

                if  opcion.isdigit(): #Comprobamos que lo que a introducido es un digito

                    opcion = int(opcion) #Le cambiamos el tipo de str a numero

                    if opcion == 1: #Opcion para añadir un producto nuevo
                        id = input("ID del producto a añadir")

                        #Añadimos al diccionario el articulo con el id que queramos
                        articulos[id] = {

                             "nombre": input("Nombre producto"),
                             "precio": int(input("Precio: ")),
                             "Stock": int(input("Stock: ")),
                             
                        }
                        print(articulos[id])
                        guardar_datos(clientes,articulos,ventas)
                       


                    elif opcion == 2:# Opcion para eliminar producto
                        id = input('Introduzca id del articulo a eliminar:\n')
                        if id in articulos:
                            console.log("[bold red]Articulo eliminado[/bold red]")
                            console.log(articulos[id], style="Red")
                            del articulos[id]
                            guardar_datos(clientes,articulos,ventas)
                        else:
                            console.log("[bold yellow]Articulo no encontrado[/bold yellow]")
                        

                    elif opcion == 3: #Ver la lista de los productos
                       #Creamos la tabla de los producto
                        tabla = Table(title="Productos",  show_header=True, border_style='bold cyan')

                        #Añadimos columnas
                        tabla.add_column("ID", style="bold cyan", justify="'right")
                        tabla.add_column("Nombre producto", style="magenta", justify="center")
                        tabla.add_column("Precio", style="magenta", justify="center")
                        tabla.add_column("Stock", style="magenta", justify="center")
                        
                        #Bucle para ver los datos de los clientes
                        for id, datos in articulos.items():
                            tabla.add_row(
                            str(id),                          # ID del artículo
                            datos['nombre'],         # Nombre del producto
                            f"{datos['precio']}€",   # Precio con símbolo de euro
                            f"{datos["Stock"]}")        #Stock del articulo
                     
                        #Mostramos la tabla
                        console.print(tabla) 
                        

                    elif opcion == 4: #Salir del bucle
                        break


                else:
                    console.log("Por favor introduce un numero", style= "bold red")


                input("Presiona enter")    
                system("cls")
        

        #Seccion de ventas
        elif texto_usuario == 3:


            while True:
                
                console.print(menu_panel3)  # Mostrar el menú de ventas
                opcion = prompt("", style=style)

                if opcion.isdigit():  # Validar que la entrada sea un número
                    opcion = int(opcion)

                    if opcion == 1:  # Registrar nueva venta
                        # Validar cliente
                        id_cliente = input("Introduce el ID del cliente: ")
                        if id_cliente not in clientes:
                            console.print("[bold red]Cliente no encontrado. Por favor, verifica el ID.[/bold red]")
                            continue

                        # Mostrar lista de productos disponibles
                        console.print("[bold cyan]Lista de productos disponibles:[/bold cyan]")
                        tabla = Table(title="Productos Disponibles", show_header=True, border_style='bold cyan')
                        tabla.add_column("ID", style="cyan")
                        tabla.add_column("Nombre", style="magenta")
                        tabla.add_column("Precio", style="green")
                        tabla.add_column("Stock", style="yellow")

                        for id_producto, datos in articulos.items():
                            tabla.add_row(id_producto, datos['nombre'], f"{datos['precio']}€", str(datos["Stock"]))

                        console.print(tabla)

                        # Seleccionar producto
                        id_producto = input("Introduce el ID del producto a vender: ")
                        if id_producto not in articulos:
                            console.print("[bold red]Producto no encontrado. Por favor, verifica el ID.[/bold red]")
                            continue

                        # Verificar stock
                        if articulos[id_producto]["Stock"] <= 0:
                            console.print("[bold yellow]No hay suficiente stock para este producto.[/bold yellow]")
                            continue

                        # Introducir cantidad
                        cantidad = int(input("Introduce la cantidad a vender: "))
                        if cantidad > articulos[id_producto]["Stock"]:
                            console.print("[bold yellow]Stock insuficiente. Solo hay disponible:[/bold yellow]", articulos[id_producto]["Stock"])
                            continue

                        # Registrar venta
                        n_venta = input("Introduce el número de la venta")
                        ventas[n_venta] = {
                            "cliente": clientes[id_cliente]["nombre"],
                            "producto": articulos[id_producto]["nombre"],
                            "cantidad": cantidad,
                            "precio_unitario": articulos[id_producto]["precio"],
                            "total": cantidad * articulos[id_producto]["precio"]
                        }
                        
                        # Actualizar stock
                        articulos[id_producto]["Stock"] -= cantidad
                        
                        console.print(f"[bold green]Venta registrada con éxito. Número de venta: {n_venta}[/bold green]")
                        
                        guardar_datos(clientes,articulos,ventas)
                        



                    elif opcion == 2:  # Eliminar venta
                        id_venta = int(input("Introduce el número de la venta a eliminar: "))
                        if id_venta in ventas:
                            # Devolver el stock al inventario
                            producto = ventas[id_venta]["producto"]
                            cantidad = ventas[id_venta]["cantidad"]

                            for id_producto, datos in articulos.items():
                                if datos["nombre"] == producto:
                                    articulos[id_producto]["Stock"] += cantidad
                                    break

                            del ventas[id_venta]

                            
                            console.print("[bold red]Venta eliminada correctamente.[/bold red]")
                        else:
                            console.print("[bold yellow]Venta no encontrada.[/bold yellow]")
                        guardar_datos(clientes,articulos,ventas)
                    elif opcion == 3:  # Ver lista de ventas
                        if not ventas:
                            console.print("[bold yellow]No hay ventas registradas.[/bold yellow]")
                        else:
                            # Mostrar tabla de ventas
                            tabla = Table(title="Ventas Registradas", show_header=True, border_style='bold cyan')
                            tabla.add_column("Número de Venta", style="cyan", justify="center")
                            tabla.add_column("Cliente", style="magenta")
                            tabla.add_column("Producto", style="green")
                            tabla.add_column("Cantidad", style="yellow")
                            tabla.add_column("Total (€)", style="bold green")

                            for n_venta, datos in ventas.items():
                                tabla.add_row(
                                    str(n_venta),
                                    datos["cliente"],
                                    datos["producto"],
                                    str(datos["cantidad"]),
                                    f"{datos['total']}€"
                                )

                            console.print(tabla)
                        input("Presiona Enter para continuar...")   
                    elif opcion == 4:  # Salir
                        break

                else:
                    console.print("[bold red]Introduce un número válido.[/bold red]")
                    input("Presiona Enter para continuar...")
                    system("cls")


        


        #Seccion de facturacion
        elif texto_usuario == 4:
            console.print(menu_panel2)
            
        #Salir del programa
        elif texto_usuario == 5:
            console.log("[bold green] Gracias por usar el programa[/bold green]")
            break
    else:
        console.print("[red]No has introducido un numero. Introduce un número.[/red]")
    input()
         
    