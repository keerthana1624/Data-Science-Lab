import matplotlib.pyplot as plt
x1=[100,250,300]
y1=[250,100,250]
plt.plot(x1,y1,label="Line1")
x2=[100,200,300]
y2=[100,300,250]
plt.plot(x2,y2,label="Line2")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Two or more lines on same plot')
plt.legend()
plt.show()
