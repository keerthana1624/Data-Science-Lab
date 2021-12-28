import matplotlib.pyplot as plt
lang = 'Java' , 'Python', 'PHP' , 'JavaScript' , 'C#', 'C++'
pop=[22.2, 17.6, 8.8,8, 7.7, 6.7]
clr=["purple", "blue", "cyan", "yellow", "orange", "red"]
explode = (0.1,0,0,0,0,0)
plt.pie(pop, explode=explode, labels=lang,colors=clr,autopct='%1.1f%%', shadow=False, startangle=140)
plt.axis('equal')
plt.show()
