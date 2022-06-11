# Construa um algoritmo que, a partir de duas cores primárias fornecidas pelo
# usuário, determine qual cor seria obtida pela mistura delas. As cores
# vermelho, azul e amarelo são chamadas de cores primárias porque não
# podem ser obtidas a partir de outras cores e, quando misturadas, resultam
# numa cor secundária, de acordo com as seguintes regras:
# a) vermelho + azul = roxo;
# b) vermelho + amarelo = laranja;
# c) azul + amarelo = verde.
# Se o usuário inserir algo diferente de “vermelho”, “azul” ou “amarelo”, o
# programa deverá exibir uma mensagem de erro. Caso contrário, o programa
# deve exibir o nome da cor secundária resultante.

print('Vamos misturar as cores? informe duas das opções que irei lhe apresentar a cor secundária resultante')

cor_primaria_1 = str(input('Digite vermelho, azul ou amarelo: '))
while cor_primaria_1 != 'vermelho' and cor_primaria_1 != 'azul' and cor_primaria_1 != 'amarelo':
    cor_primaria_1 = str(input('Erro: você digitou {}, digite uma das opções: vermelho, azul ou amarelo: '.format(cor_primaria_1)))

cor_primaria_2 = str(input('Digite vermelho, azul ou amarelo, mas não a mesma cor anterior: '))
while cor_primaria_2 != 'vermelho' and cor_primaria_2 != 'azul' and cor_primaria_2 != 'amarelo' or cor_primaria_2 == cor_primaria_1:
    cor_primaria_2 = str(input('Erro: você digitou {}, digite uma das opções: vermelho, azul ou amarelo e não repetir: '.format(cor_primaria_2)))

if cor_primaria_1 != 'amarelo' and cor_primaria_2 != 'amarelo':
    print('{} + {} = Roxo'.format(cor_primaria_1, cor_primaria_2))

elif cor_primaria_1 != 'azul' and cor_primaria_2 != 'azul':
    print('{} + {} = Laranja'.format(cor_primaria_1, cor_primaria_2))

elif cor_primaria_1 != 'vermelho' and cor_primaria_2 != 'vermelho':
    print('{} + {} = Verde'.format(cor_primaria_1, cor_primaria_2))


