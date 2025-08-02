import pandas as pd
df=pd.read_csv('costovida.csv', encoding='latin1')
#print(df.info())

filas=len(df.index)
print('Numero de filas: ',filas)

columnas=len(df.columns)
print("Numero de columnas: ",columnas)

cpromedio = df['Cost of living, 2017'].mean()
print("Costo de vida promedio: ", round(cpromedio, 2))

pais= df.loc[df['Cost of living, 2017'].idxmax(),'Countries']
ccaro = df['Cost of living, 2017'].max()
print("País con costo de vida más alto: ", pais, " con el valor de ", ccaro)

pais= df.loc[df['Cost of living, 2017'].idxmin(),'Countries']
cbajo = df["Cost of living, 2017"].min()
print("País con costo de vida más bajo: ", pais, " con el valor de ", cbajo)

peru= df[df['Countries']=='Peru']['Cost of living, 2017'].values[0]
print("Costo de vida en Perú: ", peru)

ranking=df[df['Countries']=='Peru']['Global rank'].values[0]
print("El ranking de Perú es: ", ranking)