import matplotlib.pyplot as plt
import pandas as pd
input_file = pd.read_csv('sample.csv')
country=input_file["country"]
medal_data = input_file["gold_medal"]
colors = ["cyan", "orange", "red", "green", "blue"]
explode =(0.1,0,0,0,0)
plt.pie(medal_data,labels=country, explode=explode, colors=colors, autopct='%1.1f%%' , shadow=False, startangle=140)
plt.show()
