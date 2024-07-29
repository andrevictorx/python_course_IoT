import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\Users\T-Gamer\Desktop\André\Bosch\Programação\IOT - Módulo II\CSV\company_sales_data.csv')
print(df)
sales_data=[df['facecream'].sum(),df['facewash'].sum(),df['toothpaste'].sum(),df['bathingsoap'].sum(),df['shampoo'].sum(),df['moisturizer'].sum()]
label=['Faceceam','Facewash','Toothpaste','Bathingsoap','Shampoo','Moisturizer']
plt.pie(sales_data,labels=label,autopct='%1.1f%%')
plt.title('Dados de Vendas Anual')
plt.legend(loc=[1,-0.02],fontsize=5)
plt.show()