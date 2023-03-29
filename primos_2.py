def nup(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

m = int(input("Ingrese la dimensión m de la matriz (mayor o igual a 3): "))
while m < 3:
    m = int(input("La dimensión debe ser mayor o igual a 3. Ingrese m nuevamente: "))

num_primos = []
n = 2
while len(num_primos) < m * m:
    if nup(n):
        num_primos.append(n)
    n += 1

matriz = [[0 for j in range(m)] for i in range(m)]
k = 0
for i in range(m):
    for j in range(m):
        matriz[i][j] = num_primos[k]
        k += 1

print("Matriz de números primos:")
for fila in matriz:
    print(fila)

suma_diagonal = 0
for i in range(m):
    for j in range(i, m):
        suma_diagonal += matriz[i][j]

print("La suma de los elementos en y por encima de la diagonal principal es:", suma_diagonal)
