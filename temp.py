import numpy as np

a = np.array([[1,2,3],[2,3,5],[0,1,2],[0,2,6]])

b = np.argwhere(a == 2)[:,1] 

print(b)