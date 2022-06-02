# Sabendo que há 60 segundos em um minuto, 3.600 segundos em uma hora
# e 86.400 segundo em um dia, crie um algoritmo que a partir de uma
# determinada quantidade de segundos fornecida pelo usuário, converte-a da
# seguinte maneira:
# a) Se a quantidade de segundos for maior ou igual a 60, o programa
# deverá exibir o número de minutos equivalente;
# b) Se a quantidade de segundos for maior ou igual a 3.600, o programa
# deverá exibir o número de horas equivalente;
# c) Se a quantidade de segundos for maior ou igual a 86.400, o programa
# deverá exibir o número de dias equivalente.

print('informe quantos segundos você quer converter: ')
segundos = int(input())

minutos = segundos / 60

horas = segundos / 3600

dias = segundos / 86400

if segundos >= 60 and segundos < 3600:
    print('{} segundos, equivalem a {:.4} minutos'.format(segundos, minutos))

elif segundos >= 3600 and segundos < 86400:
    print('{} segundos, equivalem a {:.6} horas'.format(segundos, horas))
    
elif segundos >= 86400:
    print('{} segundos, equivalem a {:.7} dias'.format(segundos, dias))
