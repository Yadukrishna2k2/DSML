import numpy as np
ar=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(ar)
s=np.sum(ar)
sc=np.sum(ar,axis=0)
sr=np.sum(ar,axis=1)
print("sum =",s)
print("sum of coloumn =",sc)
print("sum of row =",sr)
