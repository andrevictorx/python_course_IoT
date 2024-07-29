# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 10:29:04 2020

@author: T-Gamer
"""
import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange
df=pd.read_csv(r'C:\Users\T-Gamer\Desktop\André\Bosch\Programação\IOT - Módulo II\CSV\company_sales_data.csv')
facecream=df['facecream']
facewash=df['facewash']
month=df['month_number']
plt.bar(month-(0.2),facecream,width=0.4,align='center',label='Face Cream sale data')
plt.bar(month,facewash,width=0.4,align='edge',label='Face wash sale data')
plt.xticks(month)
plt.yticks(arange(500,4000,500))
plt.grid(True,linewidth=1,linestyle='--')
plt.legend(loc=[0.01,0.87],fontsize=7)

