# Escreva um programa que peça ao usuário para fornecer um dia, mês e o
# ano arbitrários e determine se esses dados correspondem a uma data válida.
# Não deixe de considerar que existem meses com 30 e 31 dias, e que
# fevereiro pode ter 28 ou 29 dias, dependendo se o ano for bissexto.
# Considere que um ano é bissexto quando for divisível por 4.

dia = int(input('Informe o dia: '))
mes = int(input('Informe o mês: '))
ano = int(input('Informe o ano: '))
ano_bicesto = ano % 4 

# # Segundo pesquisa disponivel em <http://xingu.fisica.ufmg.br:8087/oap/public/pas39.htm>, 
# # em 1582 que foi instituido o calendario cristão como temos hoje, antes disso o ano tinha mais dias.
if dia < 1 or dia > 31 or mes > 12 or mes < 1 or ano < 1582 or ano > 2022:
    print('Data invalida')
elif mes == 2 and dia > 29:
    print('Data invalida')
elif mes == 2 and dia == 28 and ano_bicesto != 0:
    print('Data invalida')
else:
    print('dia {}/{}/{} é uma data valida'.format(dia, mes, ano))