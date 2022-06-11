# Um carpinteiro esculpe placas personalizadas para estabelecimentos
# comerciais e deseja um programa que faça orçamentos das placas que
# produz, considerando as seguintes informações:
# a) O valor mínimo de qualquer placa é de R$ 300,00;
# b) Placas de angelim custam R$ 150,00 adicionais, mas placas de pinus não possuem nenhum custo extra;
# c) Frases com até 12 caracteres estão incluídas no valor mínimo; para
# frases maiores, são cobrados R$ 15,00 por caractere;d) Para placas com dizeres brancos ou pretos não 
# se cobra adicional, mas se ele contiver letras douradas, cobra-se R$ 60,00 a mais.

# Baseado nessas informações, construa um algoritmo que leia o número de
# um orçamento, o nome do cliente, tipo de madeira (angelim ou pinus),
# número de caracteres da mensagem e a cor dos caracteres (branco, preto ou
# dourado). Ao final, imprima todos os dados de entrada e o preço da placa orçada.
import random
print('\n-------------------------------------------------------')
print('Auto atendimento para orçamento da marcenaria do Zé')
# adicionei esses prints, para facilitar a leitura no vs code, 
# eles separam as informações importantes, ao ser executado.
print('\n-------------------------------------------------------')
# a baixo, solicitei o nome, e um gerador aleatorio, para informar um numero de orçamento, e add as variaveis 
name = str(input('Informe seu nome: '))
numero_orçamento = random.randint(1, 1000)
placa_padrao = 300
adicional_angelin = 150
adicional_dourado = 60

print('Olá ' + name + ', me chamo Zeze e vou te ajudar com seu orçamento.')

print('\n-------------------------------------------------------')
# adicionei a opção para o cliente escolhei a madeira, para não ter erro de escolha, 
# numerei as opções e depois converti em texto, para que no final apareça em texto. 
# Também já inclui a primeira variavel de preço, no if. Poderia ter incluido o while, 
# para impedir que o cliente selecione um numero diferente, mas como o codigo já esta grande, 
# não achei nescessario.
madeira_escolhida = int(input('Vamos começar escolhendo a madeira. Informe 1 para Angelim ou 2 para Pinus: '))
if madeira_escolhida == 1:
    madeira_escolhida = 'Angelim'
    placa_padrao = placa_padrao + adicional_angelin
elif madeira_escolhida == 2:
    madeira_escolhida = 'Pinus'
# a baixo pedi para o cliente informar a frase, poderia ter solicitado o numero de caracteres,
#  mas optei por fazer com a frase, contar os caracteres, diminuir os 12 gratuitos e adicionei 
# a 2° variavel de preçõ, no if. 
print('\n-------------------------------------------------------')
print('Certo, agora informe a frase que deseja na placa: ')
frase = str(input())
quantidade_caracteres = len(frase)
un = quantidade_caracteres // 1 % 10 
dez = quantidade_caracteres // 10 % 10 
dez = dez * 10
calc_caracteres = (un + dez) - 12
if calc_caracteres > 0:
    calc_caracteres = calc_caracteres * 15
    placa_padrao = placa_padrao + calc_caracteres

print('\n-------------------------------------------------------')
# aqui foi a mesma coisa, para não ter erro de escolha, 
# numerei as opções e depois converti em texto, para que no final apareça em texto. 
# Também já inclui a primeira variavel de preço, no if
cor_letras = int(input('E para finalizar, vamos escolher a cor das letras, digite 1 para Preto | 2 para Branco | 3 para Dourado: '))
if cor_letras == 1:
    cor_letras = 'Preto'
elif cor_letras == 2:
    cor_letras = 'Branco'
elif cor_letras == 3:
    cor_letras = 'Dourado'
    placa_padrao = placa_padrao + adicional_dourado

print('\n-------------------------------------------------------')

print(name +' seu orçamento possui o numero {}.'.format(numero_orçamento))

print('\n-------------------------------------------------------')

print('Você solicitou uma placa, em madeira de {} | com a frase {} | e com as letras na cor {}. '
'\nEste pedido irá lhe custar: R$ {}'.format(madeira_escolhida, frase, cor_letras, placa_padrao))
print('\n-------------------------------------------------------')


