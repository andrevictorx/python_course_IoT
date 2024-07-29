# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 11:02:08 2020

@author: T-Gamer
"""
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\T-Gamer\Desktop\André\Bosch\Programação\IOT - Módulo II\CSV\company_sales_data.csv')
profit=df['total_profit']
facewash=df['facewash']
month=df['month_number']
fig,eixo=plt.subplots(1,2,figsize=(12,4))
eixo[0].plot(month,profit,label='Profit')
eixo[0].set_title('Total Profit')
eixo[1].bar(month,facewash,label='Facewash')
eixo[1].set_title('Face Wash')