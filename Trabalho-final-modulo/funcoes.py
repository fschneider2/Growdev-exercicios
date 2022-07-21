import csv

def importar_arquivo():
    nome_arquivo = 'alunos.csv'
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
                'nome': a[i][0],
                'ano': int(a[i][1]),
                'escola': a[i][2],
                'nota_semestre_1': float(a[i][3]),
                'nota_semestre_2': float(a[i][4]),
                'media': (float(a[i][3]) + float(a[i][4])) / 2,
                'faltas': int(a[i][5]),
                'nota_exame': float(a[i][6]),
                'monitoria': (a[i][7])
            }
        )
    return info

a = importar_arquivo()

print(a)