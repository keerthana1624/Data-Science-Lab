#write a numpy program to compute sum of all elements,sum of each column and sum of each row of a given array
import numpy as np
x=np.array([[2,5],[3,7]])
print("original array is ",x)
print("sum of all elements ",np.sum(x))
print("sum of each column" ,np.sum(x,axis=0))
print("sum of each row" ,np.sum(x,axis=1))
