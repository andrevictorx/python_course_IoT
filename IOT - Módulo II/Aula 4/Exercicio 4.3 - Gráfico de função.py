# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 10:44:22 2020

@author: T-Gamer
"""
import matplotlib.pyplot as plt
from numpy import arange
x=arange(-20,21)
y=x**2
plt.plot(x,y,color='r')
plt.grid(True,alpha=0.5)


