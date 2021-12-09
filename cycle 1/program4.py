#numpy program to create a vector with values from 0 to 20 and change the sign of the numbers nin the range from 9 to 50
import numpy as np
x=np.arange(21)
print ("original vector are " ,x )

print("After changing the sign of vector")
x[(x>=9)&(x<=15)] *= -1
print(x)
