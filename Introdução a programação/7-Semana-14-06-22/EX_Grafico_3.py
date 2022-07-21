# Mostre a quantidade de homens e mulheres na base de dados.


from funcoes import importar_arquivo, dicionario_e_int
from matplotlib.pyplot import plot


# resolução do arquivo 
homem = 0
mulher = 0

dados = importar_arquivo()
info = dicionario_e_int(dados)

for i in info:
    if i['sexo'] == 'M':
        homem += 1
    else:
        mulher += 1

valores = [homem, mulher]


# grafico 
fig, ax = plt.subplloys