import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Suma de matrices
C = A + B
print("Suma de matrices:")
print(C)

# Resta de matrices
D = A - B
print("Resta de matrices:")
print(D)
# Multiplicación de matrices
E = A @ B
print("Multiplicación de matrices:")
print(E)

# Transposición de matrices
F = A.T
print("Transposición de matrices:")
print(F)
# Inversa de matrices
G = np.linalg.inv(A)
print("Inversa de matrices:")
print(G)
# Determinante de matrices
det_A = np.linalg.det(A)
print("Determinante de matrices:")
print(det_A)