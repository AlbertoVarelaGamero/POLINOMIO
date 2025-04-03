import numpy as np

def determinant_recursive(matrix):
    """Calcula el determinante de una matriz de forma recursiva."""
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for col in range(size):
        sub_matrix = [row[:col] + row[col+1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant_recursive(sub_matrix)
    return det

def determinant_iterative(matrix):
    """Calcula el determinante de una matriz de forma iterativa usando NumPy."""
    return round(np.linalg.det(np.array(matrix)))


matrix_3x3 = [
    [2, -3, 1],
    [2, 0, -1],
    [1, 4, 5]
]


print("Determinante (recursivo):", determinant_recursive(matrix_3x3))
print("Determinante (iterativo):", determinant_iterative(matrix_3x3))
