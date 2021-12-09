#write a numpy program  to  save a given array to a text file and load it
import numpy as np
import os
x=np.arange(12).reshape(4,3)
print("original array is ")
print(x)
header='col1 col2 col3'
np.savetxt('temp.txt', x,fmt="%d",header=header)
print("after loading, contents are")
result=np.loadtxt('temp.txt')
print(result)
