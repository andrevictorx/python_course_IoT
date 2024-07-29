# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 10:11:40 2020

@author: T-Gamer
"""
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\T-Gamer\Desktop\André\Bosch\Programação\IOT - Módulo II\CSV\company_sales_data.csv')
print(df)
shampoo=df['shampoo']
profit=df['total_profit']
month=df['month_number']
fig, ax1=plt.subplots(1,1,figsize=(10,4))
ax1.plot(month,shampoo,color='red',label='Shampoo sales data')
ax1.set_ylabel('Shampoo sales data',color='red')
ax1.set_xlabel('Month')
ax1.tick_params(axis='y',labelcolor='red')
ax2=ax1.twinx()
ax2.plot(month,profit)
ax2.tick_params(axis='y',labelcolor='blue')
ax2.set_ylabel('Total profit data',color='blue')
plt.xticks(month)
plt.title('Shampoo Sales Data & Total profit data')