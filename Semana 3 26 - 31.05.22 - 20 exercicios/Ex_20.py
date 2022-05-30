# Faça um programa que leia as duas notas parciais obtidas por um aluno
# numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição
# de conceitos obedece à tabela abaixo:
# Média de Aproveitamento   Conceito
# Entre 9.0 e 10.0           A
# Entre 7.5 e 8.9            B
# Entre 6.0 e 7.4            C
# Entre 4.0 e 5.9            D
# Entre 0 e 3.9              E
# O algoritmo deve mostrar na tela as notas, a média, o conceito
# correspondente e a mensagem:
# a) APROVADO se o conceito for A, B ou C.
# b) REPROVADO se o conceito for D ou E.

print('vamos calcular sua média parcial e atribuir um conceito a sua nota.')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

conceito = media
if conceito >= 9:
    conceito = 'A'
    print('Suas notas foram: {} e {} | sua média foi {} | Seu conceito foi: {}, você foi APROVADO!'.format(n1, n2, media, conceito))
elif conceito >= 7.5 and conceito <= 8.9:
    conceito = 'B'
    print('Suas notas foram: {} e {} | sua média foi {} | Seu conceito foi: {}, você foi APROVADO!'.format(n1, n2, media, conceito))

elif conceito >= 6 and conceito <= 7.4:
    conceito = 'C'
    print('Suas notas foram: {} e {} | sua média foi {} | Seu conceito foi: {}, você foi APROVADO!'.format(n1, n2, media, conceito))

elif conceito >= 4 and conceito <= 5.9:
    conceito = 'D'
    print('Suas notas foram: {} e {} | sua média foi {} | Seu conceito foi: {}, você foi REPROVADO!'.format(n1, n2, media, conceito))

elif conceito <= 3:
    conceito = 'E'
    print('Suas notas foram: {} e {} | sua média foi {} | Seu conceito foi: {}, você foi REPROVADO!'.format(n1, n2, media, conceito))
