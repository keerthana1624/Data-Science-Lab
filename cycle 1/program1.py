#write a numpy program to create a element wise comparison(greater,greater_equal,less,less_equal) of two given array
import numpy as np
a=np.array([2,11,6,3,11,21])
b=np.array([3,9,6,7,11,15])
print("original elements are ")
print(a)
print(b)
print(np.equal(a,b))
print(np.greater_equal(b,a))
print(np.greater(a,b))
print(np.less(a,b))
print(np.less_equal(a,b))

