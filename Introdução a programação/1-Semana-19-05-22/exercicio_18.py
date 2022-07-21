# Um saco de biscoitos contém 40 unidades que, de acordo com as informações do rótulo, 
# equivalem a 10 porções. Ainda de acordo com o rótulo, uma porção possui 300 calorias. 
# Baseado nessas informações, crie um algoritmo que permita ao usuário inserir o número de 
# biscoitos que ele consumiu e imprima na tela a quantidade de calorias correspondentes.
porcao = 40 / 10
un = 300 / porcao
quantas_comeu = int(input('Quantos biscoitos você comeu? '))
calorias = un * quantas_comeu
print('Se você comeu,', quantas_comeu,'biscoitos, consumiu:',calorias,' calorias.')

