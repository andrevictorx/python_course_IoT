# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 09:20:35 2020

@author: T-Gamer
"""
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\T-Gamer\Desktop\André\Bosch\Programação\IOT - Módulo II\CSV\company_sales_data.csv')
print(df)
facecream=df['facecream']
facewash=df['facewash']
toothpaste=df['toothpaste']
bathingsoap=df['bathingsoap']
shampoo=df['shampoo']
moisturizer=df['moisturizer']
month=df['month_number']
plt.plot(month,facecream,color='blue',marker='o',label='Face cream Sales Data')
plt.plot(month,facewash,color='orange',marker='o',label='Facewash Sales Data')
plt.plot(month,toothpaste,color='green',marker='o',label='Toothpaste Sales Data')
plt.plot(month,bathingsoap,color='red',marker='o',label='Bathingsoap Sales Data')
plt.plot(month,shampoo,color='purple',marker='o',label='Shampoo Sales Data')
plt.plot(month,moisturizer,color='brown',marker='o',label='Moisturizer Sales Data')
plt.axis([1,12,1000,18000])
plt.xticks(month)
plt.yticks([1000,2000,4000,6000,8000,10000,12000,15000,18000])
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc=[0.01,0.57])