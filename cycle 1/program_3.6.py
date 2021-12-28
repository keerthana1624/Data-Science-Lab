#1

import matplotlib.pyplot as plt
x=['Java' , 'Python' , 'PHP' , 'JavaScript' , 'C#' , 'c++']
popularity = [33.3, 22.2, 19.4, 15, 7, 5.7]

x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color=(0.3,0.5,0.7,0.9))
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of programming Languages\n")
plt.xticks(x_pos, x)
plt.minorticks_on()
plt.show()

#2

x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos, popularity, color='red')
plt.xlabel("Popularity")
plt.ylabel("Languages")
plt.title("Popularity of programming Language\n")
plt.yticks(x_pos, x)
plt.minorticks_on()
plt.show()

#3

x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color=['black', 'blue', 'red', 'yellow','cyan', 'orange'])
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of programing Language\n")
plt.xticks(x_pos, x)
plt.minorticks_on()
plt.show()
