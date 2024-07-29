import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\T-Gamer\Desktop\André\Bosch\Programação\IOT - Módulo II\CSV\train.csv')
print(df)
tabela=pd.pivot_table(df,values='PassengerId',index='Sex',columns='Survived',aggfunc='count')
print(tabela)
female=tabela.loc['female']
male=tabela.loc['male']
fig,eixo=plt.subplots(1,2,figsize=(8,4))
eixo[0].pie(female,labels=['Não sobreviveu','Sobreviveu'],autopct='%1.1f%%')
eixo[0].set_title('Female')
eixo[1].pie(male,labels=['Não sobreviveu','Sobreviveu'],autopct='%1.1f%%')
eixo[1].set_title('Male')
plt.show()



# =============================================================================
# values=Com base no que você vai quantificar 
# index=Coluna do DataFrame a ser coletada(Análise qualitativa)
# columns=Colunas que vão separar a análise qualitativa
# aggfunc=Função que você vai executar 
# f(x) = aggfunc(values) = contar 
# =============================================================================
