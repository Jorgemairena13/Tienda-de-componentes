#Importamos modulos
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from os import system

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

        Opcion 4 - Salir [/bold cyan]
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

menu_panel2 = Panel(
    Align.center(menu_opcion_1),
    border_style="blue",
    title="Gestion de clientes"
    )

style = Style.from_dict({
    'prompt': 'bold orange',  
    '': 'cyan bold',
})





texto_usuario = None

while texto_usuario !=6:
#Sacamos por la terminal
    console.print(menu_panel)

    texto_usuario = int(prompt('', style=style))
    system("cls")

    if texto_usuario == 1:
        console.print(menu_panel2)

    elif texto_usuario == 2:
        console.print(menu_panel2)
    
    elif texto_usuario == 3:
        console.print(menu_panel2)
    
    elif texto_usuario == 4:
        console.print(menu_panel2)
    
    elif texto_usuario == 5:
        console.print(menu_panel2)
         
    
    






input()