# Crear un diccionario vacío para almacenar la información personal
informacion_personal = {}

# Solicitar al usuario que ingrese los datos
informacion_personal["nombre"] = input("Ingresa el nombre: ")
informacion_personal["edad"] = int(input("Ingresa la edad: "))
informacion_personal["ciudad"] = input("Ingresa la ciudad: ")

# Modificar el valor asociado con la clave "ciudad"
nueva_ciudad = input("Ingresa una nueva ciudad: ")
informacion_personal["ciudad"] = nueva_ciudad

# Agregar la profesión
profesion = input("Ingresa la profesión: ")
informacion_personal["profesion"] = profesion

# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    telefono = input("Ingresa el número de teléfono: ")
    informacion_personal["telefono"] = telefono

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el diccionario resultante
print("Información Personal Final:")
print(informacion_personal)