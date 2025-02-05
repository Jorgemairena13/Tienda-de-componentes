from rich.prompt import Prompt

# Mostrar un menú
opcion = Prompt.ask("Selecciona una opción", choices=["1", "2", "3", "4"], default="1")
if opcion == "1":
    print("[green]Gestionando clientes...[/]")
elif opcion == "2":
    print("[blue]Gestionando productos...[/]")