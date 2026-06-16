import numpy as np

vec1 = np.array([1,2,3,4])
vec2 = np.array([5, 6, 7, 8])
print("Vector Addition: ",vec1+vec2)
print("Multiplication: ",vec1*vec2)
print("Dot Product: ",np.dot(vec1,vec2))
angle = np.arccos(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))
print(angle)

res = np.array(['Chinese','Indian','Italian','Mexican'])
vectorize = np.vectorize(str.upper)
vectori = np.vectorize(str.lower)
print(vectorize(res))
print(vectori(res))