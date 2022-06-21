# Implemente uma classe chamada Carro com as seguintes propriedades:
# a) Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
# b) O consumo é especificado no construtor e o nível de combustível inicial é 0.
# c) Forneça um método andar() que simula o ato de dirigir o veículo por uma certa distância, reduzindo o nível de
# combustível no tanque de gasolina.
# d) Forneça um método obter_gasolina(), que retorna o nível atual
# de combustível e forneça um metodo adicionar_gasolina(), para abastecer o tanque.

# Exemplo:
# meu_fusca = Carro(15)
# meuFusca.adicionar_gasolina(20)
# meuFusca.andar(100)
# meuFusca.obter_gasolina()

from Class import Carro

meu_fusca = Carro(15)
meu_fusca.adicionar_gasolina(20)
meu_fusca.andar(100)
meu_fusca.obter_gasolina()

