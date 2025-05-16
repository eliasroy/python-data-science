import numpy as np
#calcular la media de un array
newarrar=np.arange(1, 10)
print(newarrar.mean())

#reedimensioonar una matriz

array = np.arange(1, 13)
reshaped_array = array.reshape(3, 4)
print("Array original:")
print(array)
print("Array reestructurado:")
print(reshaped_array)

#indeacion y slicing
array = np.array([10, 20, 30, 40, 50,60])
print(f"Tercer elemento: {array[2]}")
print(f"Los tres primero {array[:3]}")
print(f"Desde el cuarto : {array[3:]}")

#mascaras booleanas
array=np.arange(1,11)
print(f"numeros pares:{array[array%2==0]}")

#suma de dos matrices

matrix1=np.array([[1,2],[3,4]])
matrix2=np.array([[1,2],[3,4]])
matrixresult=matrix1+matrix2
print(matrix1)
print(matrixresult)
