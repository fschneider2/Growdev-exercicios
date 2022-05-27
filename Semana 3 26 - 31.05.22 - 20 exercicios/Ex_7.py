# Após construir o algoritmo anterior, crie mais duas versões dele para prever
# as seguintes situações:
# a) Um aluno pode ficar em recuperação se possuir frequência suficiente
# (superior a 75%) e média superior a 5 mas inferior a 7;
# b) Caso um aluno reprove por média e faltas, sua situação deve ser
# “Reprovado por Média e Faltas” (ao invés de simplesmente
# “Reprovado por Faltas” como antes).

name = input('Digite seu nome: ')

texto = ('Olá '+ name +', vamos te ajudar a fazer o calculo, para saber se você foi aprovado ou repovado.'
'\nVamos começar calculando sua frequencia, informe quantas aulas você teve e após, em quantas delas você faltou:')

print(texto)

quantidade_aulas = int(input('Quantidade de aulas: '))

quantidade_faltas = int(input('Quantidade de faltas: '))

assiduidade = (quantidade_faltas * 100) / quantidade_aulas - 100
assiduidade = assiduidade *-1

if assiduidade >= 75:

    texto = (name +', agora vamos calcular sua média, você deve digitar suas 4 notas, de 0 a 10 ')
    print(texto)

    a = float(input('Digite a primeira nota: '))
    while a > 10:
        a = float(input('Você digitou errado, digite sua nota de 0 a 10: '))

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
        print('Parabéns, você foi aprovado! sua média foi: {}'.format(media))

    elif media > 5 and media < 7:
        print('Sua média foi: {}, logo, esta de recuperação'.format(media))

    elif media < 5:
        print('Reprovado, sua média foi: {}, a média minima é 7.'.format(media))

else:
# resolvi implementar duas vezes o calculo da média, tanto para o if quanto para o else, 
# foi a melhor forma que encontrei e chegar no resultado do exercicio. 
    texto = (name +', agora vamos calcular sua média, você deve digitar suas 4 notas, de 0 a 10 ')
    print(texto)

    a = float(input('Digite a primeira nota: '))
    while a > 10:
        a = float(input('Você digitou errado, digite sua nota de 0 a 10: '))

    b = float(input('Digite a segunda nota: '))
    while b > 10:
        b = float(input('Você digitou errado, digite sua nota de 0 a 10: '))

    c = float(input('Digite a terceira nota: '))
    while a > 10:
        c = float(input('Você digitou errado, digite sua nota de 0 a 10: '))

    d = float(input('Digite a quarta nota: '))
    while d > 10:
        d = float(input('Você digitou errado, digite sua nota de 0 a 10: '))

    media = ((a + b + c + d)/4)

    if media > 6.99 and assiduidade < 75:
        print('sua média foi: {}, porém você reprovou por faltas. Sua assiduidade foi de: {} %, quando o mmínimo era de 75%'.format(media, assiduidade))
        
    elif media < 6.99 and assiduidade < 75:
        print('Reprovado por média e faltas, sua média foi: {}, a média minima é 7. Sua presença foi {} %, o mínimo era 75%.'.format(media, assiduidade))
    
    
