# Crie um algoritmo para um jogo de adivinhação, onde o usuário tenta
# adivinhar um número aleatório gerado pelo computador. Esse número
# aleatório é inteiro e não negativo, e deve ser escolhido dentro de uma faixa
# estabelecida pelo usuário (por exemplo, o usuário pode estipular que esse
# número varie entre 0 e 10 ou entre 22 e 48, por exemplo). Após o usuário
# tentar adivinhar qual foi o número gerado, o algoritmo deve escrever esse
# número e dizer se indicar se o palpite do jogador estava correto, muito alto ou
# muito baixo.
# Dica: Para gerar um número aleatório utilize a função randint do módulo
# random.
import random

print('Vamos brincar de adivinhação? informe um número inteiro de 0 a 20: ')
numero_usuario = int(input())
while numero_usuario < 0 or numero_usuario > 20:
    numero_usuario = int(input('Informe um número de 0 - 20: '))

numero_aleatorio = random.randint(0, 20)

if numero_aleatorio == numero_usuario:
    print('você acertou! o número {} foi o sorteado'.format(numero_aleatorio))

elif numero_aleatorio > numero_usuario:
    print('Chutou baixo, o numero sorteado foi: {} e você informou: {}'.format(numero_aleatorio, numero_usuario))

else:
    print('Chutou alto, o numero sorteado foi: {} e você informou: {}'.format(numero_aleatorio, numero_usuario))

