# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 09:00:56 2020

@author: T-Gamer
"""
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\T-Gamer\Desktop\André\Bosch\Programação\IOT - Módulo II\CSV\train.csv')
idade=df['Age']
passagem=df['Fare']
plt.scatter(idade,passagem,alpha=0.5,c=passagem)
plt.show()