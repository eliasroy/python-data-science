import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#escalr dimesion 0
escalar=np.array(42)
print(type(escalar))
print(escalar)

#dimension 1 vector
vector=np.array([23,34,33,4,53,23,3])
print(vector)

#matrices 2 dimensiones

matris=np.array([[4,5,7],[1,3,5],[2, 3,4]])
print(matris)

#tensor 3 dimensiones

tensor=np.array([[[1,2],[3,4],[5,6],[7,8]]])
print(tensor)

#metodo arange que genera un rango de valores
array_range=np.arange(10)
print(array_range)

#matriz identidad
eye_matrix=np.eye(3)
print(eye_matrix)

#matriz diagonal
diagonal_matrix=np.diag([1,2,3,4,5])
print(diagonal_matrix)

#uso de random
random_array=np.random.random((3,3))
print(random_array)