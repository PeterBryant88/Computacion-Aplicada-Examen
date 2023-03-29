import numpy as np
import sys

# Reading number of unknowns
n = int(input('Enter number of unknowns: '))

k = 0
k1 = 1
k2 = 2

# Making numpy array of n x n+1 size and initializing 
# to zero for storing augmented matrix
a = np.zeros((n,n+1))

# Making numpy array of n size and initializing 
# to zero for storing solution vector
x = np.zeros(n)

# Reading augmented matrix coefficients
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))
print("Ax = b: \n",a)
        
D=np.zeros((n,n))
for i in range(n):
    for j in range(n):
        D[i][j] = a[i][j]
Deter_Delta = np.linalg.det(D)

print("Delta = ", round(Deter_Delta,3))

Dk = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        if j==k:
            Dk[i][j] = a[i][n]
        else:
            Dk[i][j] = a[i][j]
Deter_Delta_1 = np.linalg.det(Dk)

print("Delta 1 = ", round(Deter_Delta_1,3))


Dk1 = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        if j==k1:
            Dk1[i][j] = a[i][n]
        else:
            Dk1[i][j] = a[i][j]
Deter_Delta_2 = np.linalg.det(Dk1)

print("Delta 2 = ", round(Deter_Delta_2,3))


Dk2 = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        if j==k2:
            Dk2[i][j] = a[i][n]
        else:
            Dk2[i][j] = a[i][j]
Deter_Delta_3 = np.linalg.det(Dk2)

print("Delta 3 = ", round(Deter_Delta_3,3))

x1 = Deter_Delta_1/Deter_Delta
x2 = Deter_Delta_2/Deter_Delta
x3 = Deter_Delta_3/Deter_Delta

print("x1 = ", x1)
print("x2 = ", x2)
print("x3 = ", x3)