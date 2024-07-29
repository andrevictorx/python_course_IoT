# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 08:08:12 2020

@author: T-Gamer
"""
import seaborn as sns
import pandas as pd
tips=pd.read_csv(r'C:\Users\T-Gamer\Desktop\André\Bosch\Programação\IOT - Módulo II\CSV\tips.csv',sep=';')
print(tips.head(n=10))
sns.relplot(x='total_bill',y='tip',data=tips,hue='day',style='smoker',size='servings',sizes=(15,200))