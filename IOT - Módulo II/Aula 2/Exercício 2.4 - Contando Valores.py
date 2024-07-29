# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 10:35:13 2020

@author: T-Gamer
"""
import pandas as pd
import numpy as np
ser=pd.Series(np.take(list('abcdefgh'),np.random.randint(8,size=30)))
# df=pd.DataFrame(ser.value_counts())
df=pd.DataFrame(ser)
print(df[0].value_counts())