# Receba 3 notas de um aluno e peça o peso (em porcentagem) respectivamente de cada nota, 
# ao final exiba a nota final do mesmo.
nota_1 = int(input('Informe a nota 1, de 0 - 100: '))
nota_2 = int(input('Informe a nota 2, de 0 - 100: '))
nota_3 = int(input('Informe a nota 3, de 0 - 100: '))
peso_1 = int(input('Informe o peso (porcentagem) da nota 1, de 0 a 100%: '))
peso_2 = int(input('Informe o peso (porcentagem) da nota 2, de 0 a 100%: '))
peso_3 = int(input('Informe o peso (porcentagem) da nota 3, de 0 a 100%: '))
media_nota = ((nota_1 * peso_1 + nota_2 * peso_2 + nota_3 * peso_3) / (peso_1 + peso_2 + peso_3))
print('Sua media é: ', media_nota)