#Filtrado de datos: Utilizaremos funciones de NumPy para filtrar datos en arreglos. Ejemplo:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

#filtrar elementos mayores que 3
filtrados = arr[arr > 3]



#Operaciones condicionales: realizaremos operaciones condicionales en arreglos. Ejemplo:

arr1 = np.array([1, 2, 3, 4, 5, 6])

#Reemplazar elementos mayores que 3 con el valor de 10
arr1[arr1 > 3] = 10


#Ejercicio: Crea un arreglo y realiza las siguientes operaciones:
#Filtra los elementos mayores que un valor específico
#Reemplaza los elementos que cumplen una condición con un valor específico

mi_arreglo = np.array([2, 4, 6, 8, 10, 12])

filtro_mayor = mi_arreglo[mi_arreglo > 6]

mi_arreglo[mi_arreglo > 6] = 1
print(mi_arreglo)