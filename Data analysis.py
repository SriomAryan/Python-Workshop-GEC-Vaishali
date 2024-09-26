import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Chemistry.csv")

# print(df.head())
x=df.iloc[:,1]
y=df.iloc[:,2]
# print(x)
# print(y)
plt.bar(x,y)
plt.show()
