from colorama import Back,Fore
#Ver rich y questionary modulos para usar


lineas = Fore.RED+  "-" * 80

menu = f"""
{lineas}


                            Opcion 1 - Gestion clientes

                            Opcion 2 - Gestion iventario

                            Opcion 3 - Ventas

                            Opcion 4 - Facturacion

                            Opcion 5 - Reportes

                            Opcion 6 - Salir


{lineas}
"""

print(menu)
input()