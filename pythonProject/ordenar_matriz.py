def ordenar_fila(matriz, fila):
    """
    Función para ordenar una fila específica de una matriz bidimensional en orden ascendente.

    Args:
    - matriz (list): La matriz bidimensional.
    - fila (int): El índice de la fila que se desea ordenar.

    Returns:
    - list: La matriz con la fila especificada ordenada.
    """
    matriz[fila] = sorted(matriz[fila])
    return matriz


# Definir la matriz de ejemplo (3x3)
matriz_ejemplo = [
    [9, 2, 5],
    [4, 7, 1],
    [6, 3, 8]
]

# Mostrar la matriz original
print("Matriz Original:")
for fila in matriz_ejemplo:
    print(fila)

# Especificar la fila que se desea ordenar (índice 0-based)
fila_a_ordenar = 1

# Ordenar la fila especificada
matriz_ordenada = ordenar_fila(matriz_ejemplo, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la Fila Ordenada:")
for fila in matriz_ordenada:
    print(fila)