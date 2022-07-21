# Escreva um algoritmo que leia as 3 notas de um aluno e calcule a média final deste aluno.
#  Considerar que a média é ponderada e que o peso das notas é: 20%, 30% e 50%, respectivamente.
nota_1 = int(input('Informe a nota 1, de 0 - 100: '))
nota_2 = int(input('Informe a nota 2, de 0 - 100: '))
nota_3 = int(input('Informe a nota 3, de 0 - 100: '))
peso_1 = 20
peso_2 = 30
peso_3 = 50
media_nota = ((nota_1 * peso_1 + nota_2 * peso_2 + nota_3 * peso_3) / (peso_1 + peso_2 + peso_3))
print('Sua media é: ', media_nota)