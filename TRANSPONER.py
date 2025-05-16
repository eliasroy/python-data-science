import numpy as np

matriz=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

transposed_matriz=matriz.T
print("Matriz original:")
print(matriz)
print("Matriz transpuesta:")
print(transposed_matriz)

#reshape : cambia la forma de un array sin cambiar sus datos

array=np.arange(1, 13)
reshaped_array=array.reshape(3, 4)
print("Array original:")
print(array)
print("Array reestructurado:")
print(reshaped_array)


#invertir array : 

array = array[::-1]
print("Array invertido:")
print(array)

#flattenning: convierte un array multidimensional en un array unidimensional

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
flattened_array = matriz.flatten()
print("Array original:")
print(matriz)
print("Array aplanado:")
print(flattened_array)