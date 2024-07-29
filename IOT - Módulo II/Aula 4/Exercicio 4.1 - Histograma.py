# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 09:34:18 2020

@author: T-Gamer
"""
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\T-Gamer\Desktop\André\Bosch\Programação\IOT - Módulo II\CSV\company_sales_data.csv')
profit=df['total_profit']
print(profit.describe())
month=df['month_number']
plt.hist(profit,bins=20,ec='black')
