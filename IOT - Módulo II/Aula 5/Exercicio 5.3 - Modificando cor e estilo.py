# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 09:02:26 2020

@author: T-Gamer
"""
import seaborn as sns
import pandas as pd
df=pd.read_csv(r'C:\Users\T-Gamer\Desktop\André\Bosch\Programação\IOT - Módulo II\CSV\firearm.csv',sep=',')
print(df.head())
sns.relplot(x='month',y='permit',data=df,kind='line',
            color='b',height=7,aspect=1,ci=None,
            style='state',hue='state')