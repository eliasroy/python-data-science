import numpy as np

array=np.array([1, 2, 3, 4, 5])
#indexacion segundo elemento
print(array[1])

#ultimo elemento
print(array[-1])

#Indexación con Listas y Booleana: Selección de múltiples elementos utilizando listas de índices 
# o máscaras booleanas.

bool_index = array > 2
print(bool_index)
print(array[array > 2])

#Indexación con Slicing: 

array=np.random.randint(1, 10, size=(3, 3))
print(array)
print(array[0,1])

print(array[:2, :2]) #imprime los dos primeros elementos de la fila y columna