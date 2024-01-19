#Proyecto: Análisis básico de Datos con NumPy: Imaginemos que tenemos un conjunto de datos representando las ventas diarias de una tienda durante una semana. Cada fila puede representar un día y las columnas pueden incluir información como el día de la semana y las ventas en diferentes categorías de productos. 

#1- Crear un conjunto de datos: Crea un arreglo NumPy que simule un conjunto de datos para las ventas de una tienda durante una semana. 

#2- Realizar Operaciones Estadísticas: Utiliza funciones NumPy para calcular estadísticas como la suma total de las ventas, el promedio de ventas, y el día con las ventas máximas y mínimas. 

#3- Filtrar y Modificar Datos: filtra los días con ventas superiores a un umbral específico. Modifica las ventas de un día específico. 

#4- Visualizar Resultados: Utiliza la biblioteca 'matplotlib' para visualizar algunas estadísticas, como un gráfico de barras de las ventas diarias. 

import numpy as np
import matplotlib.pyplot as plt

dias = np.array(['lunes', 'martes', 'miercoles', 'jueves', 'viernes']) #defnimos en un arreglo las ventas diarias de lunes a viernes
ventas_diarias = np.random.randint(100, 200, size=(5,))
suma = np.sum(ventas_diarias) #hacemos la suma total de las ventas de la semana

media = np.mean(ventas_diarias)#calculamos la media de las ventas

dias = np.sort(ventas_diarias)#ordenamos de mayor a menor los ingresos de la semana

dia_max_ventas = dias[np.argmax(ventas_diarias)] #filtramos el día de más ingresos

dia_min_ventas = dias[np.argmin(ventas_diarias)] #filtramos el día de menos ingresos

umbral_ventas = 100
dias_con_ventas_altas = dias[ventas_diarias > umbral_ventas]
ventas_diarias[2] = 200 #modificar las ventas

#visualizar resultados:
plt.bar(dias, ventas_diarias)
plt.xlabel('dia de la semana')
plt.ylabel('ventas diarias')
plt.title('ventas diarias durante la semana')
plt.show()

#imprimir estadísticas:
print(f'suma total de ventas: {suma}')
print(f'promedio diario de ventas: {media}')
print(f'dia con ventas máximas: {dia_max_ventas}')
print(f'dia con menos ventas: {dia_min_ventas}')
print(f'dia con ventas superiores a {umbral_ventas}: {dias_con_ventas_altas}')