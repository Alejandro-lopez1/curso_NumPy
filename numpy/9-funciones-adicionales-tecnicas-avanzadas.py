#Funciones Especiales: NumPy proporciona funciones especiales, como las funciones trigonométricas inversas, exponenciales y logarítmicas. Ejemplo:

import numpy as np

#funciones especiales
seno_inverso = np.arcsin(0.5)
exponencial = np.exp(2)
logaritmo = np.log10(100)


#Manipulación de Datos Avanzados: Utilizaremos funciones avanzadas para manipular y transformar datos. Ejemplo:

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#transpner la matriz
transpuesta = np.transpose(arr)

#aplanar la matriz
aplanada = arr.flatten()


#Ejercicio: Crea una matriz y realiza las siguientes operaciones: 
#aplica funciones especiales a algunos elementos de la matriz.
#utiliza funciones avanzadas para manipular y transformar la matriz, como la transpolación y aplanamiento

arr1 = np.array([[2, 3, 4], [2, 4, 6], [7, 8, 9]])



trans = np.transpose(arr1)

aplanada1 = arr1.flatten()
print(aplanada1)
