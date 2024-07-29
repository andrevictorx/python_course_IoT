# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 09:21:15 2020

@author: T-Gamer
"""
import seaborn as sns
import pandas as pd
df=pd.read_csv(r'C:\Users\T-Gamer\Desktop\André\Bosch\Programação\IOT - Módulo II\CSV\diamonds.csv',sep=';')
print(df.head())
sns.catplot(x='color',y='price',kind='swarm',data=df)
sns.catplot(x='clarity',y='carat',kind='swarm',data=df)

