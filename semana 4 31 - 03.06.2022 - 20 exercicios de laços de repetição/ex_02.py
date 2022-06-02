# Escrever um programa que lê um valor N inteiro e positivo e que calcula seu
# valor fatorial. Ex: 5! = 5 * 4 * 3 * 2 * 1

fatorial = 1 

num = int(input('Digite um numero que irei lhe apresentar o fatorial: '))

for n in range(1, num+1):
        fatorial *= n
print(f'o fatorial de {num} é {fatorial}')
