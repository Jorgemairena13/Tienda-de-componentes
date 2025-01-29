from rich.progress import Progress, BarColumn, TextColumn
import time

# Crear un objeto Progress manualmente
progress = Progress(
    TextColumn("[bold blue]Cargando tienda de componentes[/]"),
    BarColumn(),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
)

progress.start()  # Iniciar el progreso
tarea = progress.add_task("Progreso", total=100)

for i in range(100):
    time.sleep(0.05)  # Simula una tarea en proceso
    progress.update(tarea, advance=1)

progress.stop()  # Detener el progreso

