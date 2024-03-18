def buscar_valor(matriz, valor):
    """
    Función para buscar un valor específico en una matriz bidimensional.

    Args:
    - matriz (list): La matriz bidimensional en la que buscar el valor.
    - valor: El valor que se desea buscar en la matriz.

    Returns:
    - tuple: Una tupla que contiene la posición del valor si se encuentra, o None si no se encuentra.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor:
                return i, j
    return None


# Definir una matriz de ejemplo (3x3)
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Definir el valor a buscar
valor_a_buscar = 5

# Buscar el valor en la matriz
posicion = buscar_valor(matriz_ejemplo, valor_a_buscar)

# Mostrar el resultado
if posicion:
    print(f"El valor {valor_a_buscar} se encontró en la posición {posicion}.")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")