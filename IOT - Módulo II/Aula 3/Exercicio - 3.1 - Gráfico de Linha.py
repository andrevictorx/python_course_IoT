# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 08:40:04 2020

@author: T-Gamer
"""
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\T-Gamer\Desktop\André\Bosch\Programação\IOT - Módulo II\CSV\company_sales_data.csv')
print(df)
profit= df.loc[:,['total_profit']]
month=df['month_number']
print(month)
plt.plot(month,profit)
plt.title('Company profit per month')
plt.ylabel('Profit')
plt.xlabel('Month Number')
plt.xticks(month)
plt.yticks([100000,200000,300000,400000,500000])
plt.show()
plt.savefig('Exercício-3.1.png')