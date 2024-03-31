# Escritura de Archivo de Texto
# Abrir el archivo en modo de escritura
with open("my_notes.txt", "w") as file:
    # Escribir al menos tres líneas de notas personales
    file.write("Nota 1: Este es un recordatorio importante.\n")
    file.write("Nota 2: No olvides hacer la tarea de Python.\n")
    file.write("Nota 3: Comprar leche en el camino a casa.\n")

# Lectura de Archivo de Texto
# Abrir el archivo en modo de lectura
with open("my_notes.txt", "r") as file:
    # Leer el contenido del archivo línea por línea
    for line in file.readlines():
        # Mostrar en la consola cada línea leída
        print(line.strip())