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

#Combinamos el menu y el titulo
menu_combinado = f"{titulo}\n\n{menu_contenido}"



#Aqui le aplicamos las propiedades al menu
menu_panel = Panel(
    Align.center(menu_combinado),
    border_style="blue"
)
#Propiedades para el menu de la opcion 1
menu_panel2 = Panel(
    Align.center(menu_opcion_1),
    border_style="blue",
    title="Gestion de clientes"
    )
#Estilo para los prompt
style = Style.from_dict({
    'prompt': 'bold orange',  
    '': 'cyan bold',
})

#Diccionario para ir añadiendo los clientes con sus datos
clientes = {}

texto_usuario = None

while texto_usuario !=6:
#Sacamos por la terminal
    console.print(menu_panel)

    texto_usuario = prompt('', style=style)
    system("cls")

    if texto_usuario.isdigit():
        texto_usuario = int(texto_usuario)
        if texto_usuario == 1:
            while True:

                console.print(menu_panel2)
                opcion = prompt('', style=style)
                
                if opcion.isdigit():
                    opcion = int(opcion)
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
                system("cls")





        elif texto_usuario == 2:
            console.print(menu_panel2)
        
        elif texto_usuario == 3:
            console.print(menu_panel2)
        
        elif texto_usuario == 4:
            console.print(menu_panel2)
        
        elif texto_usuario == 5:
            console.print(menu_panel2)
    else:
        console.print("[red]No has introducido un numero. Introduce un número.[/red]")
    input()
         
    