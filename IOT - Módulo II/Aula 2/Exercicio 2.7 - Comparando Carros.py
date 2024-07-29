# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:20:14 2020

@author: T-Gamer
"""
import pandas as pd
df=pd.read_csv(r'CSV\Cars93_miss.csv').loc[:,['Manufacturer','Make','Price','MPG.city','Type','Passengers']]
df=df[df['Passengers']==5].sort_values(by='MPG.city')
df=df.dropna().tail(n=10).sort_values(by='Price')
df=df.head()
print(df)