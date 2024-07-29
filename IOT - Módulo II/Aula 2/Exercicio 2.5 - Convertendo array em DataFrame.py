# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 10:46:25 2020

@author: T-Gamer
"""
import pandas as pd
import numpy as np
array=np.random.randint(1,10,35).reshape(7,5)
print(array)
df=pd.DataFrame(array)
print(df)
