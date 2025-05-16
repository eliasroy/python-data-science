import numpy as np

A= np.array([[1, 2], [3, 4]])
B= np.array([[5, 6], [7, 8]])
# Suma de matrices
C= A + B
print(f"Suma de matrices:{C}")

# Resta de matrices
D= A - B
print(f"Resta de matrices:{D}")

# Multiplicación de matrices
E= A @ B
print(f"Multiplicación de matrices:{E}")

# Transposición de matrices
F= A.T
print(f"Transposición de matrices:{F}")

# Inversa de matrices
G= np.linalg.inv(A)
print(f"Inversa de matrices:{G}")

# Determinante de matrices
det_A= np.linalg.det(A)
print(f"Determinante de matrices:{det_A}")

#Resolver sistemas de ecuaciones lineales
#ax+by=c

b=np.array([1,2])
x=np.linalg.solve(A,b)
print(f"Solución del sistema de ecuaciones lineales:{x}")
