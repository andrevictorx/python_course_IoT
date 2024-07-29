# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 19:53:08 2020

@author: T-Gamer
"""
import pandas as pd
import numpy as np
ser1=pd.Series(list('abcdefghijklmnopqrstuvxwyz'))
ser2=pd.Series(np.arange(26))
df=pd.DataFrame(ser1,ser2)
print(df)
