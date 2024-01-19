#Funciones universales básicas: Las funciones universales son operaciones que se aplican a cada elemento de un arreglo. Ejemplo:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

#Funciones universales
cuadrado = np.square(arr) #Elevar al cuadrado
raiz_cuadrada = np.sqrt(arr) #Raiz cuadrada
logaritmo = np.log(arr) #Logaritmo natural
#print(logaritmo)

#Funciones Trigonométricas: NumPy también ofrece funciones trigonométricas como seno, coseno y tangente. ejemplo:
angulos = np.array([0, np.pi/2, np.pi])

seno = np.sin(angulos)
coseno = np.cos(angulos)
tangente = np.tan(angulos)
#print(tangente)

#Ejercicio: crea un nuevo arreglo con valores numéricos y utiliza funciones universales de NumPy para:
#calcular el cuadrado de cada elemento
#encontrar la raiz cuadrada de cada elemento
#calcular el logaritmo de cada elemento
#utilizar al menos una función trigonométrica. 

mi_array = np.array([2, 4, 6, 8, 10])
mi_square = np.square(mi_array)
mi_raiz = np.sqrt(mi_array)
mi_logaritmo = np.log(mi_array)


mi_angulo = np.array([2, 4, 6, 8, 10])
seno1 = np.sin(mi_angulo)
coseno1 = np.cos(mi_angulo)
tangente1 = np.tan(mi_angulo)
print(coseno1)