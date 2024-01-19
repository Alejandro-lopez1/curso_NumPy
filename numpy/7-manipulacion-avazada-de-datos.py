#Concatenación de arreglos: La concatenación es la unión de dos o más arreglos. Ejemplo:
import numpy as np

#crear dos arreglos
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

#concatenar arreglos horizontalmente
concatenacion_horizontal = np.concatenate((arr1, arr2), axis=0)



#División de arreglos: La división implica dividir un arreglo en partes más pequeñas. Ejemplo:
arr = np.array([1, 2, 3, 4, 5, 6])

#dividir el arreglo en tres partes
partes = np.split(arr, 3)



#Ejercicio: Crea dos arreglos y realiza las siguientes operaciones:
#concatenar los arreglos horizontalmente
#dividir uno de los arreglos en dos partes iguales

mi_array = np.array([10, 20, 30, 40])
mi_array2 = np.array([50, 60, 70, 80])

#concatenación
concat = np.concatenate((mi_array, mi_array2), axis=0)

#dividiendo el primer arreglo en dos partes
division1 = np.split(mi_array2, 2)
print(division1)
