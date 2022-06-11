# Numa determinada escola, os critérios de aprovação são os seguintes:
# a) O aluno deve ter, no máximo, 25% de faltas;
# b) A nota final deve ser igual ou superior a 7,00.
# Construa um algoritmo para ler as notas que um aluno tirou nos 4 bimestres,
# o número total de aulas e o número de faltas, mostrando ao final a situação
# do aluno como sendo “Aprovado”, “Reprovado por Faltas” e “Reprovado por
# média”, considerando que a reprovação por faltas se sobrepõe a reprovação
# por nota.

name = input('Digite seu nome: ')
# inclui algumas informações extras, para personalizar meu codigo, como o nome e o texto
texto = ('Olá '+ name +', vamos te ajudar a fazer o calculo, para saber se você foi aprovado ou reprovado.'
'\nVamos começar calculando sua frequencia, informe quantas aulas você teve e após, em quantas delas você faltou:')

print(texto)

quantidade_aulas = int(input('Quantidade de aulas: '))

quantidade_faltas = int(input('Quantidade de faltas: '))

assiduidade = (quantidade_faltas * 100) / quantidade_aulas - 100
assiduidade = assiduidade *-1
# fiz o calculo de assiduidade, como queria a informação de presença, e não de falta, fiz o calculo matematico a cima
if assiduidade >= 75:
# sabendo que a reprovação por faltas se sobressai, caso o aluno reprove por faltas, nem irá solicitar o calculo de média.
    print('Você teve {} % de presença'.format(round(assiduidade, 1)))

    texto = (name +', agora vamos calcular sua média, você deve digitar suas 4 notas, de 0 a 10 ')

    a = float(input('Digite a primeira nota: '))
    while a > 10:
        a = float(input('Você digitou errado, digite sua nota de 0 a 10: '))
# while é para não da erro na média, forçando o aluno a colocar uma nota de 0 - 10.
    b = float(input('Digite a segunda nota: '))
    while b > 10:
        b = float(input('Você digitou errado, digite sua nota de 0 a 10: '))

    c = float(input('Digite a terceira nota: '))
    while c > 10:
        c = float(input('Você digitou errado, digite sua nota de 0 a 10: '))

    d = float(input('Digite a quarta nota: '))
    while d > 10:
        d = float(input('Você digitou errado, digite sua nota de 0 a 10: '))

    media = ((a + b + c + d)/4)

    if media > 6.99:
        print('Parabéns, você foi aprovado! sua média foi {}'.format(media))

    else:
        print('Reprovado, sua média foi {}, a média minima é 7.'.format(media))

else:
    print('Você foi reprovado por falta, possui {} % de presença, quando o minimo era de 75%'.format(round(assiduidade, 1)))






