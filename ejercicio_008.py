import pandas as pd

def ordenarAprobados(notas):
    for key, value in dict(notas).items():
        if value < 6:
            del notas[key]
    return pd.Series(notas).sort_values(ascending=False)

def inicio():
    notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5,'Luis': 5}
    print(ordenarAprobados(notas))
    
inicio()