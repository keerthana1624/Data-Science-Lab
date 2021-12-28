import matplotlib.pyplot as plt
import pandas as pd
maths = [88,92,80,89,100,80,60,100,80,34 ]
science = [35,79,79,48,100,88,32,45,20,30]
marks_range = [10,20,30,40,50,60,70,80,90,100]
plt.scatter(marks_range,maths,label='maths marks',color='r')
plt.scatter(marks_range,science,label='science marks',color='g')
plt.title('Scatter Plot')
plt.xlabel('Marks Range')
plt.ylabel('Marks Scored')
plt.legend()
plt.show()
