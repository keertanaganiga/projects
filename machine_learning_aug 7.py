import numpy as np
import pandas as pd


import matplotlib.pyplot as plt
import seaborn as sns





get_ipython().run_line_magic('matplotlib', 'inline')





df=pd.read_csv("USA_Housing.csv")




df.head()





df.info()




df.describe()





df.columns





sns.pairplot(df)




sns.distplot(df['Price'])





df.corr()





sns.heatmap(df.corr(),annot=True,cmap='coolwarm')

