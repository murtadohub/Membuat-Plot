import datetime
import pandas as pd 
import matplotlib.pyplot as plt 

dataset = pd.read_csv('data.csv') # untuk membaca file data.csv

#untuk menambah kolom order_month
dataset['order_month'] = dataset['order_date'].apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))

#untuk menambah kolom gmv
dataset['gmv'] = dataset['item_price']*dataset['quantity']

#untuk membuat data Agregat pada data.csv
monthly_amount = dataset.groupby('order_month')['gmv'].sum().reset_index()

#untuk membuat grafik dg matplotlib ada 2 cara :
#cara 1
# plt.plot(monthly_amount['order_month'], monthly_amount['gmv'])

#cara 2
fig = plt.figure(figsize=(15,5))#untuk mengubah ukuran grafik
dataset.groupby(['order_month'])['gmv'].sum().plot(color='green', marker='o',linestyle='-.', linewidth=3)

print('ukuran dataset: %d baris dan %d kolom\n' % dataset.shape)#mencetak kolom order_month
print('Lima data teratas:')
print(dataset.head())#mencetak lima data teratas
print(monthly_amount)#mencetak hasil Agregat order_month dengan gmv
plt.title('Monthly  GMV YEAR 2019', loc='center',pad=20, fontsize=15, color='red')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total GMV  (in Billions)', fontsize=15)
plt.grid(color='yellow', linestyle=':', linewidth=1)
plt.ylim(ymin=0)
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))
plt.text(0.45,0.72,'gmv meningkat secara signifikan pada oktober 2019',transform=fig.transFigure, color='blue')
plt.savefig('monthly_gmv.png', quality=95)
plt.show()#untuk menmapilkan grafik
