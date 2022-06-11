# Sabendo que o lucro anual de uma empresa é, tipicamente, 23% do total de vendas, 
# crie um programa que solicite ao usuário que entre com o valor projetado do total de vendas e, 
# em seguida, calcule e exiba o lucro que deve ser obtido com esse valor.

valor_projetado_vendas = float(input('Informe o valor projetado de vendas: R$ '))
lucro = (valor_projetado_vendas / 100) * 23
print('O lucro estimado é de: R$ ', lucro)
