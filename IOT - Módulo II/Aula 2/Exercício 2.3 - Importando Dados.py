# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 10:02:56 2020

@author: T-Gamer
"""
import pandas as pd
df=pd.read_csv(r'CSV\BostonHousing.csv').loc[:,['crim','medv']]
print(df.head(14))
