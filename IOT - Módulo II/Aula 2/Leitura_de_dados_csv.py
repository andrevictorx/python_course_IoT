# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 09:31:31 2020

@author: T-Gamer
"""
#Leitura de Dados - CSV
import pandas as pd
df=pd.read_csv(r'CSV\dados.csv', sep=',', encoding='latin_1')
print(df.head())