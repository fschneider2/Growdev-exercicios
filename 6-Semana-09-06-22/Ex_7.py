#  Faça uma função que recebe por parâmetro o tempo de duração da produção de uma peça em 
# uma fábrica, expressa em segundos e exibe esse tempo em horas, minutos e segundos

import os

os.system('clear')


tempo = int(input('Informe o tempo em segundos: '))

def horas_minutos_segundos(a):

    if a >= 86400:
        dias = a // 86400
        a -= (dias * 86400)
        horas = a // 3600
        a = a - (horas * 3600)
        minutos = a // 60
        segundos = a % 60

    elif a >= 3600 and a < 86400:
        dias = 0
        horas = a // 3600
        a = a - (horas * 3600)
        minutos = a // 60
        segundos = a % 60

    elif a >= 60 and a < 3600:
        dias = 0
        horas = 0
        minutos = a // 60
        segundos = a % 60

    else:
        dias = 0
        horas = 0
        minutos = 0
        segundos = a

    return f'{tempo} segundos = {dias}dias, {horas} horas, {minutos} minutos, {segundos} segundos'

calculo = horas_minutos_segundos(tempo)
print(calculo)
    

