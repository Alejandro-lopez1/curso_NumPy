#creación de arreglos: En Python, NumPy proporciona el tipo de dato 'array' que nos permite crear arreglos multidimensionales. Puedes crear arreglos unidimensionales, bidimensionales, etc

#Ejemplo de creación de arreglos:
import numpy as np

#crear un arreglo unidimensional
arr_uni = np.array([1, 2, 3, 4, 5])

#crear un arreglo bidimensional
arr_bi = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#Operaciones aritméticas básicas: NumPy permite realizar operaciones aritméticas elementos a elemento en arreglos.

#Ejemplo:
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

#suma
suma_resultado = arr1 + arr2

#multiplicación
multiplicación_resultado = arr1 * arr2


#indexación y rebanado: Acceder a elementos individuales o subconjuntos de un arreglo. 
#Ejemplo:
arr = np.array([1, 2, 3, 4, 5])

#acceder al primer elemento:
primer_elemento = arr[0]

#rebanar el conjunto desde el segundo elemento en adelante:
subconjunto = arr[1:]

#Ejercicio: crea dos arreglos unidimensionales con valores numéricos y realiza las siguientes operaciones:
#suma de los arreglos
#multiplica uno de los arreglos por un escalar
#accede a un elemento específico de cada arreglo
#rebanar uno de los arreglos para obtener solo los primeros tres elementos

#suma de los arreglos
Arr1 = np.array([1, 2, 3])
Arr2 = np.array([7, 8, 9])

sum_array = Arr1 + Arr2
#print(sum_array) 

#multiplicación de un arreglo por una escalar
multipl_escalar = Arr2 * 3
#print(multipl_escalar)


#rebanar uno de los arreglos para obtener solo el primer elemento
sub = Arr2[:1]
print(sub)

