# Faça um programa completo utilizando funções e classes que:

# a)Possui uma classe chamada Ponto, com os atributos x e y.

# b)Possui uma classe chamada Retângulo,com os atributos largura e altura.

# c)Possui uma função para imprimir os valores da classe Ponto.

# d)Possui uma função para encontrar o centro de um retângulo.

# e)Você deve criar alguns objetos da classe Retangulo.

# f)Cada objeto deve ter um vértice de partida,por exemplo,o vértice inferior esquerdo do retângulo, que deve ser um 
# objeto da classe Ponto.

# g)A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x
# e y para o centro do objeto.

# h)O valor do centro do objeto deve ser mostrado na tela

from Class import Ret, Ponto

ret = Ret()

ret.ponto1 = Ponto(4,3)
ret.ponto2 = Ponto(10,7)

ponto_central1 = ret.centro()

ponto_central1.exibe_valores()