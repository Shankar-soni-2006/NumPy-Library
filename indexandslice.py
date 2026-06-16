import numpy as np

# arr = np.array([1,2,3,4,5,6,7,8,9,10])
# print("Slicing:",arr[2:7])
# print("step:",arr[1:8:2])

# arr2d = np.array([[1, 2, 3], 
#                   [4, 5, 6,], 
#                   [7, 8, 9]])
# print("Specific element:",arr2d[1,2])
# print("Specific row:", arr2d[1, :])
# print("Specific column:", arr2d[:, 2])

# unsort = np.array([3,6,9,8])
# unsort2d = np.array([[3,1],
#                     [1,2],
#                     [2,3]])
# print(np.sort(unsort))
# print(np.sort(unsort2d,axis = 1))

# num = np.array([1,2,3,4,5,6,7,8,9,10])
# even = num[num%2==0]
# print(even)

# mask = num > 5 
# print(num[mask])

# place = np.where(mask)
# print(place)
# print(num[place])
# print(np.where(mask,"true","false"))

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# print(arr1+arr2) output:- [5,7,9];
# print(np.concatenate((arr1,arr2)))
# print(np.delete(arr1,2))

org = np.array([[1,2],[3,4]])

# new = np.array([[5,6]])
# print(org,"\n",new)
# print(np.vstack((org,new)))
# print(np.hstack((org,new.T)))

print("Array after Deleted",np.delete(org,[0],axis=0))
