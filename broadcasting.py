import numpy as np

"""prices=np.array([100,200,300,400,500])
discount=np.array([0.9])
# Apply discount to each price
discounted_prices = prices * discount
print(discounted_prices)

prices= np.random.randint(100, 1000, size=(3, 3))
discount= np.array([10,20,30])
# Apply discount to each price
discounted_prices = prices+ discount
print(prices)
print(discounted_prices)

"""

# Comparaciones
array2=np.array([1,2,3,4,5])
print(np.all(array2 > 0))

print(np.any(array2 > 4))


#concatenacion
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

concat=np.concatenate((array1, array2))
print(concat)

#concat vertical

sateced_v=np.vstack((array1, array2))
print(sateced_v)

#concat horizontal
sateced_h=np.hstack((array1, array2))
print(sateced_h)


#division de array
array3 = np.arange(1, 10)
split_array = np.split(array3, 3)
print(array3)
print(split_array)