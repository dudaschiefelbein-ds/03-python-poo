import pandas as pd

cidades= [
    {'nome': 'Distrito Federal','uf':'DF' , 'populacao': 3121212 },
    {'nome': 'São Paulo','uf':'SP' , 'populacao': 198211212 },
    {'nome': 'Rio de Janeiro','uf':'RJ' , 'populacao': 5121212 },
    {'nome': 'Recife','uf':'PE' , 'populacao': 1090212 },
]

dataFrame=pd.DataFrame(cidades)
ordenada= dataFrame.sort_values(by='populacao', ascending=False)
print(ordenada)
print()
print(ordenada.head(2))
#print(ordenada.head(2)['nome']) O Python pega o DataFrame ordenado, 
# filtra as 2 primeiras linhas com .head(2) 
# e imprime somente coluna 'nome' com as  duas primeiras linhas.