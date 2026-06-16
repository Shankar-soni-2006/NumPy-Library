import numpy as np

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.random.rand(3,3)
arr3 = np.zeros((4,4))

np.save('array1.npy',arr1)
np.save('array2.npy',arr2)
np.save('array3.npy',arr3)

load_arr1 = np.load('array1.npy')
print(load_arr1)