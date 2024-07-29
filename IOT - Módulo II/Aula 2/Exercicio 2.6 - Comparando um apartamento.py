# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 10:53:15 2020

@author: T-Gamer
"""
import pandas as pd
df=pd.read_csv(r'CSV\dados.csv', sep=',', encoding='latin_1')
print(df[(df['quartos']>=2) & (df['bairro']=='Botafogo')].sort_values(by='preco').head(n=5))


