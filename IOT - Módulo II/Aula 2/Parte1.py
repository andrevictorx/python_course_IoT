# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 07:43:52 2020

@author: T-Gamer
"""
import pandas as pd
df_alunos=pd.DataFrame({'Aluno':['Ron','Hermione','Draco','Harry','Ginny'],
                  'Faltas':[3,2,1,3,1],
                  'Prova':[5,10,6,7,9],
                  'Seminário':[7,9.5,7.5,8,9]})
df_alunos=df_alunos[:]
print(df_alunos)
df_alunos.to_csv('aulas.csv')