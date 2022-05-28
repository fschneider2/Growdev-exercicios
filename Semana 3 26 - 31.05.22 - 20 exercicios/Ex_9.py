# Escreva um programa que peça ao usuário para fornecer um dia, mês e o
# ano arbitrários e determine se esses dados correspondem a uma data válida.
# Não deixe de considerar que existem meses com 30 e 31 dias, e que
# fevereiro pode ter 28 ou 29 dias, dependendo se o ano for bissexto.
# Considere que um ano é bissexto quando for divisível por 4.

print('#'*53)
print('Certo, agora informe a frase: ')
frase = str(input())
quantidade_caracteres = len(frase)
un = quantidade_caracteres // 1 % 10 
dez = quantidade_caracteres // 10 % 10 
dez = dez * 10
calc_caracteres = (un + dez) - 12
if calc_caracteres > 0:
    calc_caracteres = calc_caracteres * 15
