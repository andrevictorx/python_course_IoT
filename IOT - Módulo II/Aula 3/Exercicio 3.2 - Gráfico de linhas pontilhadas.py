# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 09:05:02 2020

@author: T-Gamer
"""
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\T-Gamer\Desktop\André\Bosch\Programação\IOT - Módulo II\CSV\company_sales_data.csv')
profit=df['total_profit']
month=df['month_number']
plt.plot(month,profit,linestyle='--',color='red',marker='o',markerfacecolor='black',linewidth=3)
plt.axis([0,12,0,50000])
plt.xticks(month)
plt.yticks([200000,300000,400000,500000])
plt.title('Lucro total por mês')
plt.xlabel('Número do Mês')
plt.ylabel('Lucro Total')


