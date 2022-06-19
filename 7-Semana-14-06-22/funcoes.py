# Utilize as seguintes faixas etárias nos exercícios em que for necessário.
# ● Jovens, 18 a 25 anos
# ● Adultos, 26 a 59 anos
# ● Idosos, igual ou maior que 60 anos

# Utilize o arquivo ‘compras.csv’ como base para resolver os seguintes
# exercícios.
import csv

def importar_arquivo():
    nome_arquivo = 'compras.csv'
    f = open(nome_arquivo, encoding= 'utf-8') #Criando outra variavel para para abrir o arquivo, e usando o enconding para codificar o conteudo do arquivo, corrigindo acentos e 'ç' por exemplo.
    dados = csv.reader(f, delimiter= ',') # pegando os dados abertos na variavel f, e delimitando a quebra de conteudo para cada ,.
    dados = list(dados) # Alterando o formato de dados para uma lista
    return dados

def dicionario_e_int(a):
    info = [] # Função para converter a lista em dicionario e algumas colunas em int
    for i in range(1, len(a)): 
        info.append(
            {
                'nome': a[i][0],
                'sobrenome': a[i][1],
                'idade': int(a[i][2]),
                'sexo': a[i][3],
                'compra': int(a[i][4]),
                'ano': int(a[i][5]),
                'pagamento': a[i][6]
            }
        )
    return info

def filtrar_anos(a):
    anos = [] # função para filtrar os anos 
    for i in a:
        anos.append(i['ano'])
    anos = sorted(set(anos)) # limpando a lista e removendo informações repetidas.
    return anos

def converter_RS(val): # converter um valor monetario em float para moeda RS
    a = '{:,.2f}'.format(float(val))
    b = a.replace(',','v')
    c = b.replace('.',',')
    return c.replace('v','.')