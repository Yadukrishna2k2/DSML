import numpy as np
ar1=np.array([[1,2,3],[4,5,6],[7,8,9]])
ar2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("array 1")
print(ar1)
print("array 2")
print(ar2)
if np.array_equal(ar1,ar2):
    print("Equal")
else:
    print("Not Equal")
