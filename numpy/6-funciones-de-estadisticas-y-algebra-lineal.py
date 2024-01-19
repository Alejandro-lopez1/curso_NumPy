#Funciones de aĺgebra lineal: Utilizaremos funciones de álgebra linealmás avanzadas en NumPy. Ejemplo:
import numpy as np

#crear una matriz
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#calcular la norma euclidiana de la matriz
norma_euclidiana = np.linalg.norm(matriz)

#calcular los valores propios y vectores propios
valores_propios, vectores_propios = np.linalg.eig(matriz)


#Funciones de estadísticas: Exploraremos más funciones estadísticas en NumPy. Ejemplo:

arr = np.array([1, 2, 3, 4, 5])

#calcular la mediana y la desviación estándar
mediana = np.median(arr)
desviacion_estandar = np.std(arr)




#Ejercicio: crea una matriz y realiza las siguientes operaciones:
#calcular la norma euclidiana de la matriz
#calcular los valores propios y vectores propis de una matriz
#utilizar funciones estadísticas como la mediana y la desviación estandar en un arreglo.add()

#creando la nueva matriz
mi_matriz = ([[2, 4, 6], [1, 3, 5], [7, 8, 9]])

#calculando la norma euclidiana
calc_euclidian = np.linalg.norm(mi_matriz)

#calculando los valores propios y vectores propios de la matriz
valores_propios1, vectores_propios1 = np.linalg.eig(mi_matriz)

#calculando la mediana y la desviacion estandar
mediana1 = np.median(mi_matriz)
desv_estandar = np.std(mi_matriz)

print(desv_estandar)