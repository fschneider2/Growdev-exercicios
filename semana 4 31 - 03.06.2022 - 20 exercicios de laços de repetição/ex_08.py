# Escreva um programa que leia a idade e salário de 10 pessoas. Informe em
# seguida:
# a) Qual é a média de idade entre as pessoas?
# b) Quantas pessoas há por faixa etária, considerando:
# i)jovens < 18
# ii)18 <= adultos < 60
# iii)idosos >= 60
# c) Em seguida, mostre qual é a faixa etária que acumula o maior salário.

# criei listas vazias para receber todas as infomrações necessarias, já pensando nas saidas que preciso apresentar.
contador = 1
jovens = []
adultos = []
idosos = []
sal_jovens = []
sal_adultos = []
sal_idosos = []
lista_salario = []
lista_idades = []

print('--'*13)

while contador <= 10:
# entrada de dados e armazenagem de informações nas respectivas listas, que usarei no inal para dar as saidas e realizar os calculos.
    idade = int(input('Informe sua idade: '))
    lista_idades.append(idade)
    if idade < 18:
        jovens.append(idade)
    elif idade >= 18 and idade < 60:
        adultos.append(idade)
    elif idade >= 60:
        idosos.append(idade)

    salario = float(input('Informe seu salario: R$ '))
    lista_salario.append(salario)  
    if idade < 18:
        sal_jovens.append(salario)
    elif idade >= 18 and idade < 60:
        sal_adultos.append(salario)
    elif idade >= 60:
        sal_idosos.append(salario)

    contador += 1
# calc média das idades
media_idades = sum(lista_idades) / len(lista_idades)
# calculo para saber as médias de salario, o enunciado não pede isso, porém achei fundamental para que o calculo de faixa etaria com maior salario faça sentido, 
# tendo em vista que podemos ter uma amostra muito maior de uma determinada faixa etária, 8 jovens, 1 adulto e 1 idoso, por exemplo.
#  Nesse caso, o somatorio tenderia a ser maior para os jovens. logo fiz uma media com base na amostra, e também apresentei o somatorio, que o enunciado pedia, 
# era possivel apresentar uma saida para o somatorio, mas não achei necessario.
media_salarioJovens = sum(sal_jovens) / len(jovens)
media_salarioAdulto = sum(sal_adultos) / len(adultos)
media_salarioIdosos = sum(sal_idosos) / len(idosos)

print(f'A média de idade do grupo é de : {media_idades} anos')

print('--'*13)

print(f'A faixa etária de jovens com menos de 18 anos possui {len(jovens)} pessoas  \nA faixa etária de adultos entre 18 e 60 anos, possui {len(adultos)} pessoas \nA faixa etária de idosos maiores de 60 anos, possui {len(idosos)} pessoas') 

print('--'*13)
# poderia utilizar a mesma regra e fazer uma saida para a faixa etária que acumula o maior salário.
if media_salarioJovens > media_salarioAdulto and media_salarioJovens > media_salarioIdosos:
    print(f'A faixa etária que acumula a maior média de salario são os dos Jovens. Com um salario médio de R$ {media_salarioJovens} que somou R$ {sum(sal_jovens)}')

elif media_salarioAdulto > media_salarioIdosos and media_salarioAdulto > media_salarioJovens:
    print(f'A faixa etária que acumula a maior média de salario são os dos Adultos. Com um salario médio de R$ {media_salarioAdulto} que somou R$ {sum(sal_adultos)}')

else:
    print(f'A faixa etéria que acumula a maior média de salario são os dos Idosos. Com um salario médio de R$ {media_salarioIdosos} que somou R$ {sum(sal_idosos)}')