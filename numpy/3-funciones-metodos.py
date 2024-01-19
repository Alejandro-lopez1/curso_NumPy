#Funciones y estadísticas básicas: NumPy proprciona funciones que permiten realizar operaciones estadísticas en arreglos. ejemplo:

import numpy as np
arr = np.array([3, 7, 1, 5, 10])

#calcular la suma de los elementos:
suma = np.sum(arr)

#calcular la media de los elementos:
media = np.mean(arr)

#calcular el valor máximo y el mínimo:
maximo = np.max(arr)
minimo = np.min(arr)

#método 'reshape()': se utiliza para cambiar la forma de un arreglo. Ejemplo:
arR = np.array([1, 2, 3, 4, 5, 6])

#cambiar la forma del arreglo
nueva_forma = arR.reshape(2, 3)
print(nueva_forma)

#Ejercicio: crea un arreglo unidimensional con al menos 7 elementos numéricos. Luego utiliza las funciones de NumPy para: 
#calcular la suma y media de los elementos
#encontrar el valor máximo y mínimo
#cambiar la forma del arreglo a una matriz de 2x3

MiArray = np.array([1, 2, 3, 4, 5, 6, 7])
mi_suma = np.sum(MiArray)

mi_max = np.max(MiArray)

mi_min = np.min(MiArray)

MiArray_ajustado = MiArray[:-1]
matriz_2x3 = MiArray_ajustado.reshape(2, 3)

print("Arreglo original: ")
print(MiArray)

print("Matriz 2x3")
print(matriz_2x3)
