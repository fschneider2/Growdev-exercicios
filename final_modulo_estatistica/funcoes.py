import csv

def importar_arquivo():
    nome_arquivo = 'dados_modulo_estatistica.csv'
    f = open(nome_arquivo, encoding= 'utf-8') 
    dados = csv.reader(f, delimiter= ',') 
    dados = list(dados)
    info = dicionario_e_int(dados)
    return info

def dicionario_e_int(a):
    info = [] 
    for i in range(1, len(a)): 
        info.append(
            {
                'semana': a[i][0],
                'dia': a[i][1],
                'temperatura': float(a[i][2])
            }
        )
    return info
