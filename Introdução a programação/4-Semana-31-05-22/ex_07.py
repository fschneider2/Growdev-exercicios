# Escreva um programa que leia 10 valores e encontre o maior e o menor
# deles. Mostre o resultado.

# apresentado as variaveis, onde criei um contador para conseguir finalizar o while, 
# e criei uma lista vazia para armazenar os numeros
contador = 1
lista_numeros =[]

# enquanto o contador estiver menor ou igual ao 10, ele vai pegar os numeros e armazenar na lista 
while contador <= 10:

    numero = int(input('Digite 10 valores, no fim vou lhe informar o maior e o menor: '))
    lista_numeros.append(numero)
    contador += 1

# saidas solicitadas.
print(f'O maior numero digitado foi: {max(lista_numeros)}')
print(f'O menor numero digitado foi: {min(lista_numeros)}')