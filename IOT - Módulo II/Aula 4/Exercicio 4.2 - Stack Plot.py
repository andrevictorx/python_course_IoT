# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 10:21:37 2020

@author: T-Gamer
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv(r'C:\Users\T-Gamer\Desktop\André\Bosch\Programação\IOT - Módulo II\CSV\company_sales_data.csv')

month=df['month_number'].tolist()
facecream=df['facecream'].tolist()
facewash=df['facewash'].tolist()
toothpaste=df['toothpaste'].tolist()
bathingsoap=df['bathingsoap'].tolist()
shampoo=df['shampoo'].tolist()
moisturizer=df['moisturizer'].tolist()

y=np.vstack([facecream,facewash,toothpaste,bathingsoap,shampoo,moisturizer])

labels=['Facecream','Facewash','Toothpaste','Bathingsoap','Shampoo','Moisturizer']

fig,ax=plt.subplots()

ax.stackplot(month,facecream,facewash,toothpaste,bathingsoap,shampoo,moisturizer,\
             colors=['m','c','r','k','g','y'],labels=labels)
plt.title('All product sales data using stack plot')
plt.xticks(month)
plt.xlabel('Month Number')
plt.ylabel('Sale units in Number')
plt.legend(loc=[0.01,0.57])
plt.axis([1,12,0,30000])
plt.show()

