# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 10:01:25 2020

@author: olv2ct
"""
arquivo= open('arquivo.txt','r')
def localizar(palavra):
    print('-'*30)
    print ('LOCALIZADOR DE PALVRAS')
    print('-'*30)
    numero=0
    palavra=str(' {} '.format(palavra))
    for linha in arquivo:
        print(linha)
        num=linha.count(palavra.strip())
        print(num)
        numero=numero+num
    print('\nNesse texto a palavra{}aparece {} vezes.'.format(palavra,numero))
    
        
localizar('It')