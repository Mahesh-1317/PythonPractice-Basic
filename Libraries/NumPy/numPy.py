import numpy as np

arr = np.array([1,2,4,6,7])
arr2 = np.array([[5,8,0], [20,12,43], [45,7,18]])

print(arr2.shape)
print(arr2.dtype)
print(arr2.ndim)

#   Some Methods
zeros = np.zeros((3,4))
print(zeros)

ones = np.ones((2,4))
print(ones)

rng = np.arange(0,50,5)
print(rng)

lin = np.linspace(0,1,11)
lin2 = np.linspace(0,17,7)
print(lin)
print(lin2)

random = np.random.randint(40,100,(4,3))
print(random)