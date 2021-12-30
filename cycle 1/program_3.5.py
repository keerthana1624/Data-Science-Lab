import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,5,0.01)
plt.subplot(3,1,1)
plt.title('sin')
plt.plot(x,np.sin(x))
plt.subplot(3,1,2)
plt.title('cos')
plt.plot(x,np.cos(x))
plt.subplot(3,1,3)
plt.title('straight')
plt.plot(x,x)
plt.show()
