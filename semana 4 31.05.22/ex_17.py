# Crie um programa para que retorne o somatório de todos os números entre 1
# e um valor fornecido pelo usuário. Por exemplo, se o usuário fornecer o
# número 4, o computador deverá calcular o somatório 1+ 2 + 3 + 4 = 10.

numero = int(input('Digite um numero: '))
lista_v = []
for i in range(1, numero + 1):
    lista_v.append(i)
print(f'O somatorio de {numero} é = {sum(lista_v)}')
