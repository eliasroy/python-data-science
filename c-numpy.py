import numpy as np

array=np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(array)
#imprime el numero de dimensiones
print(array.ndim)
#imprime la forma de la matriz
print(array.shape)
#imprime el tipo de dato
print(array.dtype)

#uint8 es un tipo de dato que ocupa 1 byte
#float32 es un tipo de dato que ocupa 4 bytes
#float64 es un tipo de dato que ocupa 8 bytes

#numero entero
entero=np.array(3,dtype=np.uint8)
print(entero)

#numero flotante
double = np.array([1,2,3], dtype='d')
print(double)

#conversion de entero a flotante
entero=entero.astype(np.float64)
print(entero)

array=np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
sum=np.sum(array)
print(sum)

mean=np.mean(array)
print(mean)

std=np.std(array)
print(std)

min=np.min(array)
print(min)
max=np.max(array)
print(max)