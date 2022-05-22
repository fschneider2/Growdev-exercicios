print('Informe quantos anos, meses e dias você tem')
idade_pessoa_anos = int(input('Anos: '))
idade_pessoa_meses = int(input('Meses: '))
idade_pessoa_dias = int(input('Dias: '))
idade_dias = (idade_pessoa_anos * 365) + (idade_pessoa_meses * 31) + idade_pessoa_dias
print('Você já viveu', str(idade_dias), 'dias')