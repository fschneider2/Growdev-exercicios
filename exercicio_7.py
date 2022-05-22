# Escreva um algoritmo que leia a idade de uma pessoa expressa em anos, 
# meses e dias e mostre-a expressa apenas em dias. Considere ano = 365 dias, 
# mês = 31 dias..

print('Informe quantos anos, meses e dias você tem')
idade_pessoa_anos = int(input('Anos: '))
idade_pessoa_meses = int(input('Meses: '))
idade_pessoa_dias = int(input('Dias: '))
idade_dias = (idade_pessoa_anos * 365) + (idade_pessoa_meses * 31) + idade_pessoa_dias
print('Você já viveu', str(idade_dias), 'dias')