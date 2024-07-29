# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 08:29:43 2020

@author: T-Gamer
"""
import matplotlib.pyplot as plt
plt.plot([10,20,30,40],[15,40,75,90],linestyle='--',color='r',marker='s',linewidth=3.0)
plt.axis([0,50,0,100])
plt.xticks([10,20,30,40])
plt.yticks([20,40,60,80])
plt.grid(True,linewidth=1,linestyle='--')
plt.savefig('Gráfico1')
plt.show()