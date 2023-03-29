import numpy as np

# Definimos la matriz de coeficientes A y el vector de términos independientes b
A = np.array([[0.25, 0.15, 0],
              [0.45, 0.5, 0.75],
              [0.30, 0.35, 0.25]])

b = np.array([1.5, 5, 3])

# Calculamos el determinante de la matriz de coeficientes A
detA = np.linalg.det(A)

# Calculamos el determinante de las matrices A1, A2 y A3
A1 = A.copy()
A1[:, 0] = b
detA1 = np.linalg.det(A1)

A2 = A.copy()
A2[:, 1] = b
detA2 = np.linalg.det(A2)

A3 = A.copy()
A3[:, 2] = b
detA3 = np.linalg.det(A3)

# Calculamos las soluciones x, y, z utilizando el método de Cramer
x = detA1 / detA
y = detA2 / detA
z = detA3 / detA

# Imprimimos las soluciones
print("A =", x)
print("B =", y)
print("C =", z)
