import numpy as np

# tensor = np.array(
#    [[[1,2],[3,4]],
#     [[5,6],[7,8]]])

# print(tensor)

# arr = np.array([[1,2,3],
#                [4,5,6]])

# print(arr.shape)
# print(arr.ndim)
# print(arr.size)
# print(arr.dtype)

#Array Reshaping
arr = np.arange(12)
print(arr)
reshaped = arr.reshape(3,4)
print(reshaped)
flattened = reshaped.flatten()
print(flattened)
raveled = reshaped.ravel()
print(raveled)
transposed = reshaped.T
print(transposed)
