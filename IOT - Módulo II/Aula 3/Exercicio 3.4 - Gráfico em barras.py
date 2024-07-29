# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 10:11:24 2020

@author: T-Gamer
"""
import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\T-Gamer\Desktop\André\Bosch\Programação\IOT - Módulo II\CSV\company_sales_data.csv')
print(df)
bathingsoap=df['bathingsoap']
month=df['month_number']
plt.bar(month,bathingsoap)
plt.title('Bathinsoap sales data')
plt.grid(True,linewidth=1,linestyle='--')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.xticks(month)
plt.yticks([2000,4000,6000,8000,10000,12000,14000])
plt.savefig('Exercicio 3.4 - Gráfico em barras.png')
