# Construa um algoritmo que leia uma data qualquer (dia, mês e ano) e calcule
# a data do próximo dia. Lembre-se que em anos bissextos o mês de fevereiro
# tem 29 dias. Lembre-se que um ano é bissexto quando for divisível por 4.

dia = int(input('Informe o dia: '))
mes = int(input('Informe o mês: '))
ano = int(input('Informe o ano: '))
ano_bicesto = ano % 4 

# # Sjuntei todas as possibilidades de data invalida. 
if dia < 1 or dia > 31 or mes > 12 or mes < 1 or ano < 1582 or mes == 2 and dia > 29 or mes == 2 and dia == 28 and ano_bicesto != 0:
    print('Data invalida')
# Se for uma data valida, preferi iniciar pelo mês de fevereiro, depois inclui todas as possibilidades exigidas.
elif dia >= 1 and dia <= 27 and mes == 2:
    dia = dia + 1
    print('Amanhã é dia {}/{}/{}'.format(dia, mes, ano))

elif dia == 28 and mes == 2:
    dia = 1
    mes = mes + 1
    print('Amanhã é dia {}/{}/{}'.format(dia, mes, ano))

elif dia >= 1 and dia <= 30:
    dia = dia + 1
    print('Amanhã é dia {}/{}/{}'.format(dia, mes, ano))

elif dia == 31 and mes == 1 or mes < 12:
    dia = 1
    mes = mes + 1
    print('Amanhã é dia {}/{}/{}'.format(dia, mes, ano))

elif dia == 31 and mes == 12:
    dia = 1
    mes = 1
    ano = ano + 1
    print('Amanhã é dia {}/{}/{}'.format(dia, mes, ano))
