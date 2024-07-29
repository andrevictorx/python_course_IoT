# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 08:31:10 2020

@author: T-Gamer
"""
import seaborn as sns
import pandas as pd
tips=pd.read_csv(r'C:\Users\T-Gamer\Desktop\André\Bosch\Programação\IOT - Módulo II\CSV\tips.csv',sep=';')
sns.relplot(x='total_bill',y='tip',style='smoker',data=tips,hue='smoker')
sns.relplot(x='total_bill',y='tip',size='servings',sizes=(20,200),hue='servings',data=tips)
