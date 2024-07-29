# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 10:05:28 2020

@author: T-Gamer
"""
import matplotlib.pyplot as plt
y=[20,50,30]
x=range(len(y))
plt.bar(x,y,width=0.4, color='yellow', ec='black', align='center')
plt.show()
