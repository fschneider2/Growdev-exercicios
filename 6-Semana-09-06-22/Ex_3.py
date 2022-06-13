# Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string em um formato por extenso. Opcionalmente, valide a data
# e retorne NULL caso a data seja inválida

import os

from datetime import datetime

os.system('clear')

def data_por_extenso(a):

    data = a.split('/')

    if int(data[1]) == 1:
        data[1] = 'Janeiro'

    elif int(data[1]) == 2:
        data[1] = 'Fevereiro'

    elif int(data[1]) == 3:
        data[1] = 'Março'

    elif int(data[1]) == 4:
        data[1] = 'Abril'

    elif int(data[1]) == 5:
        data[1] = 'Maio'

    elif int(data[1]) == 6:
        data[1] = 'Junho'

    elif int(data[1]) == 7:
        data[1] = 'Julho'

    elif int(data[1]) == 8:
        data[1] = 'Agosto'

    elif int(data[1]) == 9:
        data[1] = 'Setembro'

    elif int(data[1]) == 10:
        data[1] = 'Outubro'

    elif int(data[1]) == 11:
        data[1] = 'Novembro'

    elif int(data[1]) == 12:
        data[1] = 'Dezembro'

    mensagem = f'{data[0]} de {data[1]} de {data[2]}'

    return mensagem

def validando_data(b):
    try:
        datetime.strptime(b, '%d/%m/%Y')
        return 'Data Valida'
    except ValueError:
        return 'Data Invalida'


print('¨§'*30)

entrada_usuario = input('\nInforme uma data no formato DD/MM/AAAA: ')

print('_'*60)

resposta_data =  data_por_extenso(entrada_usuario)

data_valida_invalida = validando_data(entrada_usuario)

print(f'\n{resposta_data} é uma {data_valida_invalida}\n')


