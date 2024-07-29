# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 09:06:47 2020

@author: T-Gamer
"""
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\T-Gamer\Desktop\André\Bosch\Programação\IOT - Módulo II\CSV\company_sales_data.csv')
toothpaste=df['toothpaste']
month=df['month_number']
plt.scatter(month,toothpaste,label='Tooth paste Sales data',alpha=0.9)
plt.xticks(month)
plt.xlabel('Month Number')
plt.ylabel('Number of units Sold')
plt.title('Tooth paste Sales Data')
plt.grid(True,linestyle='--')
plt.legend(loc=[0.01,0.9])
