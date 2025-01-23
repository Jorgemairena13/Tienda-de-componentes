#Importamos modulos
from rich import print 
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from os import system
from rich.table import Table

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

                                Opcion 5 - Reportes

                                Opcion 6 - Salir
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

Opción 3 - Ver detalles de producto

Opción 4 - Lista de todos los productos

Opción 5 - Buscar producto

Opción 6 - Salir
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
menu_panel2 = Panel(
    Align.center(menu_opcion_2),
    border_style="blue",
    title="Gestion de productos"
    )

#Estilo para los prompt
style = Style.from_dict({
    'prompt': 'bold orange',  
    '': 'cyan bold',
})

#Diccionario para ir añadiendo los clientes con sus datos
clientes = {}
#Diccionario para ir añadiendo los articulos 

articulos = {
    "id_1": {"nombre": "Procesador", "precio": 100},

    "id_2": {"nombre": "Tarjeta gráfica", "precio": 200},

    "id_3": {"nombre": "Memoria RAM", "precio": 80},

    "id_4": {"nombre": "Disco Duro", "precio": 60},

    "id_5": {"nombre": "SSD", "precio": 120},

    "id_6": {"nombre": "Placa Base", "precio": 150},

    "id_7": {"nombre": "Fuente de Alimentación", "precio": 70},

    "id_8": {"nombre": "Sistema de Refrigeración", "precio": 50}
}


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


                    elif opcion == 2:
                        # Eliminar cliente
                        nif = input('Introduzca NIF del cliente a eliminar:\n')
                        if nif in clientes:
                            console.log("[bold red]Cliente eliminado[/bold red]")
                            console.log(clientes[nif], style="Red")
                            del clientes[nif]
                        else:
                            console.log("[bold yellow]Cliente no encontrado[/bold yellow]")
                        input('Enter para continuar')


                    elif opcion == 3:
                        # Mostrar cliente concreto que quiera 
                        nif = input("Introduzca NIF del cliente: ")
                        if nif in clientes:
                            print(clientes[nif])
                        else:
                            print("Cliente no encontrado")
                        input("Enter para continuar")
                        


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

                        console.print(tabla)
                        input()
                            

                    elif opcion == 5:
                        break
                else:
                    console.print("[red]No has introducido un numero. Introduce un número.[/red]")
                input()
                system("cls")




        #Opcion 2 del menu principal
        elif texto_usuario == 2:
            #Creamos el bucle para que este siempre abierta 
            while True:
                console.print(menu_panel2) #Mostramos menu
                opcion = prompt("", style=style)

                if  opcion.isdigit():

                    opcion = int(opcion)

                    if opcion == 1: #Opcion para añadir un producto nuevo
                        id = input("Que producto vas a añadir")

                        articulos[id] = {

                             "nombre": input("Nombre producto"),
                             "precio": int(input("Precio: ")),
                             
                        }
                        print(articulos[id])
                        input()


                    elif opcion == 2:# Opcion para eliminar producto
                        id = input('Introduzca id del articulo a eliminar:\n')
                        if id in articulos:
                            console.log("[bold red]Articulo eliminado[/bold red]")
                            console.log(articulos[id], style="Red")
                            del articulos[id]
                        else:
                            console.log("[bold yellow]Articulo no encontrado[/bold yellow]")
                        input('Enter para continuar')

                    elif opcion == 3: #Ver los detalles del producto
                        console.log("Ver detalles de productos")

                    elif opcion == 4: #Ver la lista de los productos
                       
                        tabla = Table(title="Productos",  show_header=True, border_style='bold cyan')

                        #Añadimos columnas
                        tabla.add_column("ID", style="bold cyan", justify="'right")
                        tabla.add_column("Nombre producto", style="magenta", justify="center")
                        tabla.add_column("Precio", style="magenta", justify="center")
                        
                        #Bucle para ver los datos de los clientes
                        for id, datos in articulos.items():
                            tabla.add_row(
                            str(id),                         # ID del artículo
                            datos['nombre'],         # Nombre del producto
                            f"€{datos['precio']}")   # Precio con símbolo de euro
                     
                           

                    

                        console.print(tabla)
                        input()

                    elif opcion == 5: #Buscar productos
                        console.log("Buscar productos")


                else:
                    console.log("Por favor introduce un numero", style= "bold red")


                input()    
                system("cls")
        


        elif texto_usuario == 3:
            console.print(menu_panel2)
        
        elif texto_usuario == 4:
            console.print(menu_panel2)
        
        elif texto_usuario == 5:
            console.print(menu_panel2)
    else:
        console.print("[red]No has introducido un numero. Introduce un número.[/red]")
    input()
         
    