# Escrever um programa que lê um valor N inteiro e positivo e que calcula seu
# valor fatorial. Ex: 5! = 5 * 4 * 3 * 2 * 1

# um contador, com o nome de fatorial, so par fazer um pouco diferente
fatorial = 1 
# Entrada
num = int(input('Digite um numero que irei lhe apresentar o fatorial: '))
# um forma alternativa a apresentada em aula, onde o mentor utilizou o - 1, 
# para regradir. Porem nesse caso so tenho a reposta final, sem conseguir armazenar o passo a passo do calculo
for n in range(1, num+1):
        fatorial *= n
print(f'o fatorial de {num} é {fatorial}')
