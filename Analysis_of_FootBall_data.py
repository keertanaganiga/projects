#!/usr/bin/env python



import numpy as np
import pandas as pd
import os
from matplotlib import pyplot as plt
import seaborn as sns

os.getcwd()

fifa=pd.read_csv('fifa_data.csv')


fifa.head()


for col in fifa.columns:
    print(col)

fifa.shape

fifa['nationality'].value_counts()


fifa['age'].value_counts()


fifa['nationality'].value_counts()[0:10]


fifa['nationality'].value_counts()[0:5].keys()


plt.figure(figsize=(8,5))
plt.bar(list(fifa['nationality'].value_counts()[0:5].keys()),list(fifa['nationality'].value_counts()[0:5]),color='green')
plt.show()


players_salary=fifa[['short_name','wage_eur']]


players_salary.head()


players_salary=players_salary.sort_values(by=['wage_eur'],ascending=False)


players_salary.head()


plt.figure(figsize=(8,5))
plt.bar(list(players_salary['short_name'])[0:5],list(players_salary['wage_eur'])[0:5],color=['purple','orange','yellow','green','red'])
plt.show()


fifa['nationality']=='Germany'


Germany=fifa[fifa['nationality']=='Germany']
Germany.head(10)

Germany.sort_values(by=['height_cm'],ascending=False).head()


Germany[['short_name','wage_eur']].sort_values(by=['wage_eur'],ascending=False).head()


player_shooting=fifa[['short_name','shooting']]


player_shooting.sort_values(by=['shooting'],ascending=False).head()

player_defending=fifa[['short_name','nationality','defending','club']]


player_defending.sort_values(by=['defending'],ascending=False).head()

player=fifa[fifa['club']=='Liverpool']


player.sort_values(by=['wage_eur'],ascending=False).head()


player.sort_values(by=['shooting'],ascending=False).value_counts()





