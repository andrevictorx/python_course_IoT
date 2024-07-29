# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 11:34:15 2020

@author: T-Gamer
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\T-Gamer\Desktop\André\Bosch\Programação\IOT - Módulo II\CSV\company_sales_data.csv')
print(df)
bathingsoap=df['bathingsoap']
facewash=df['facewash']
month=df['month_number']

fig,eixo=plt.subplots(2,1,sharex=True,figsize=(6,4))

eixo[0].plot(month,bathingsoap,color='black',marker='o',label='Sales data of Bathingsoap')
eixo[0].set_title('Sales Data of Bathingsoap')

eixo[1].plot(month,facewash,color='red',marker='o',label='Sales data of Facewash')
eixo[1].set_title('Sales Data of Facewash')

plt.xticks(month)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.savefig('Exercício 3.6 - Subplot.jpg')