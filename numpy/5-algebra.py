#Operaciones de Algebra lineal con NumPy. Multiplicación de matrices: NumPy facilita la multiplicación de matrices mediante la función 'np.dot()' o el operador '@'. Ejemplo:

import numpy as np

#rcear matrices
matriz_a = np.array([[1, 2],[3, 4]])
matriz_b = np.array([[5, 6], [7, 8]])

#multiplicación de matrices
resultado_multiplicación = np.dot(matriz_a, matriz_b)
#print(resultado_multiplicación) 

#Inversa y Determinante: NumPy proporciona funciones para calcular la inversa y el determinante de una matriz. Ejemplo:
matriz = np.array([[1, 2], [3, 4]])

#calcular la inversa de la matriz
inversa = np.linalg.inv(matriz)

#calcular el determinante de la matriz
determinante = np.linalg.det(matriz)
#print(inversa)

#Ejercicio: crea dos matrices cuadradas y realiza las siguientes operaciones:
#multiplicación de matrices
#calcular la inversa de una de las matrices
#calcular el determinante de la otra matriz

mi_matriz1 = ([[10, 20], [30, 40]])
mi_matriz2 = ([[5, 7], [9, 11]])

mi_multiplicación = np.dot(mi_matriz1, mi_matriz2)
#print(mi_multiplicación)

inversa1 = np.linalg.inv(mi_matriz1)
determinante1 = np.linalg.det(mi_matriz2)

print(determinante1)
