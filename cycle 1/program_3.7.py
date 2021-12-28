import numpy as np
import matplotlib.pyplot as plt

tot_grp=5
m_means=(22,30,35,35,26)
w_means=(25,32,30,35,29)

fig, ax = plt.subplots()
index = np.arange(tot_grp)
width=0.35
opacity=0.8

rect1 = plt.bar(index, m_means,width,alpha=opacity,color='g',label='men')
rect2 = plt.bar(index + width, w_means,width,alpha=opacity,color='r',label='women')
plt.xlabel('Person')
plt.ylabel('Scores')
plt.xticks(index + width, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.legend()

plt.tight_layout()
plt.show()
