import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('costovida.csv')

# Los 10 países con el costo de vida más alto
altos = df.sort_values(by='Cost of living, 2017', ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.barh(altos['Countries'], altos['Cost of living, 2017'])
plt.title('Los 10 países con mayor costo de vida')
plt.xlabel('Costo de vida')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('PaisesCostoAlto.jpg')
plt.show()

# Los 10 países con el costo de vida más bajo
bajos = df.sort_values(by='Cost of living, 2017', ascending=True).head(10)
plt.figure(figsize=(10, 6))
plt.barh(bajos['Countries'], bajos['Cost of living, 2017'], color='green')
plt.title('Top 10 países con menor costo de vida')
plt.xlabel('Costo de vida')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('PaisesCostoBajo.jpg')
plt.show()

# El costo de vida de los países de América
america = [
    'Argentina', 'Bolivia', 'Brazil', 'Canada', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominican Republic',
    'Ecuador', 'El Salvador', 'Guatemala', 'Honduras', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 'Peru',
    'Uruguay', 'United States', 'Venezuela'
]

Am = df[df['Countries'].isin(america)]
plt.figure(figsize=(12, 7))
plt.barh(Am['Countries'], Am['Cost of living, 2017'], color='orange')
plt.title('Costo de vida en países de América')
plt.xlabel('Costo de vida')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('PaisesAmerica.jpg')
plt.show()