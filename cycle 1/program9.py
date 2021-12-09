#write a numpy program to create a 4x4 array with random values,now create a new array from the said array swapping first and last rows
import numpy as np
x=np.random.randint(100,size=(4,4))
print(x)
print("after swapping")
x[[3,0]]=x[[0,3]]
print(x)
