import statistics
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Abre el archivo, se necesita el archivo d2.txt del Repositorio
with open('d2.txt', 'r') as archivo:
    # Inicializa las tres listas
    lista_num1 = []
    lista_num2 = []
    lista_car = []

    # Lee el archivo línea por línea
    for linea in archivo:
        # Separa las columnas
        columna = linea.split(',')

        # Almacena los datos en las listas correspondientes
        lista_num1.append(float(columna[0]))
        lista_num2.append(float(columna[1]))
        lista_car.append(columna[2].strip()) # Elimina los espacios en blanco y saltos de línea

# Calcula la media y desviación estándar de las listas numéricas
media_num1 = statistics.mean(lista_num1)
media_num2 = statistics.mean(lista_num2)
desv_est_num1 = statistics.stdev(lista_num1)
desv_est_num2 = statistics.stdev(lista_num2)

# Calcula la probabilidad de que una persona se encuentre dentro de la primera desviación estándar en ambas columnas
prob_num1 = len([i for i in lista_num1 if media_num1 - desv_est_num1 <= i <= media_num1 + desv_est_num1]) / len(lista_num1)
prob_num2 = len([i for i in lista_num2 if media_num2 - desv_est_num2 <= i <= media_num2 + desv_est_num2]) / len(lista_num2)

# Imprime los resultados
print("Estatura: ")
print("Media de la estatura:", media_num1)
print("Desviación estándar de la estatura:", desv_est_num1)
print("Probabilidad de que una persona se encuentre dentro de la primera desviación estándar de la estatura:", prob_num1)

print("\nTalla de calzado: ")
print("Media de la talla de calzado del análisis:", media_num2)
print("Desviación estándar de la talla de calzado del análisis:", desv_est_num2)
print("Probabilidad de que una persona se encuentre dentro de la primera desviación estándar de la talla de calzado del análisis:", prob_num2)

# Crea el histograma de la lista_num1
plt.hist(lista_num1, bins=20, density=True, alpha=0.6, color='blue')

# Calcula la función de densidad de probabilidad normal para la lista_num1
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, media_num1, desv_est_num1)
plt.plot(x, p, 'k', linewidth=2)

# Crea el histograma de la lista_num2
plt.hist(lista_num2, bins=20, density=True, alpha=0.6, color='red')

# Calcula la función de densidad de probabilidad normal para la lista_num2
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, media_num2, desv_est_num2)
plt.plot(x, p, 'k', linewidth=2)


# Aproximación lineal para todos los datos
coef = np.polyfit(lista_num1, lista_num2, 1)
linea_aprox = np.polyval(coef, lista_num1)

# Calcula la pendiente de la aproximación lineal
pendiente = coef[0]
independiente = coef[1]

# Imprime la pendiente de los datos globales
print("\nAproximación lineal de los datos globales: ")
print("Pendiente:", pendiente)
print("Intercepto:", independiente)

# Filtra los datos por género "Femenino"
datos_femeninos = [(num1, num2) for num1, num2, car in zip(lista_num1, lista_num2, lista_car) if car == 'Femenino']
lista_num1_femenino, lista_num2_femenino = zip(*datos_femeninos)

# Ajusta una línea a los datos de lista_num1_femenino y lista_num2_femenino
coeficientes_femenino = np.polyfit(lista_num1_femenino, lista_num2_femenino, 1)
pendiente_femenino = coeficientes_femenino[0]
intercepto_femenino = coeficientes_femenino[1]

print("\nAproximación lineal de los datos clasificados Femenino: ")
print("Pendiente de Femenino:", pendiente_femenino)
print("Intercepto de Femenino:", intercepto_femenino)

# Filtra los datos por género "Masculino"
datos_masculino = [(num1, num2) for num1, num2, car in zip(lista_num1, lista_num2, lista_car) if car == 'Masculino']
lista_num1_masculino, lista_num2_masculino = zip(*datos_masculino)

# Ajusta una línea a los datos de lista_num1_masculino y lista_num2_masculino
coeficientes_masculino = np.polyfit(lista_num1_masculino, lista_num2_masculino, 1)
pendiente_masculino = coeficientes_masculino[0]
intercepto_masculino = coeficientes_masculino[1]

print("\nAproximación lineal de los datos clasificados Masculino: ")
print("Pendiente de Masculino:", pendiente_masculino)
print("Intercepto de Masculino:", intercepto_masculino)

plt.show()
