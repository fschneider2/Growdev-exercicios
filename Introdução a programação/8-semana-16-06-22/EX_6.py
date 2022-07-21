# Faça um programa completo utilizando classes e métodos que:
# a) Possua uma classe chamada BombaCombustivel, com no mínimo esses atributos:
# i)tipo_combustivel.
# ii)valor_litro
# iii)quantidade_combustivel
                            
# b) Possua no mínimo esses métodos:
# i) abastecer_por_valor() – método onde é informado o valor a ser abastecido e mostra a quantidade de litros 
# que foi colocada no veículo
# ii) abastecer_por_litro() – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
# iii) alterar_valor() –altera ovalor do litro do combustível.
# iv)alterar_combustivel() – altera o tipo do combustível.
# v)alterar_quantidade_combustivel() – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

from Class import BombaCombustivel

posto = BombaCombustivel('Gasolina', 7.39, 100)

posto.abastecer_por_litro(50)
print(posto.quantidade_combustivel)

posto.abastecer_por_valor(369.5)
print(posto.quantidade_combustivel)

posto.alterar_combustivel('alcool')

posto.abastecer_por_litro(10)
print(posto.quantidade_combustivel)
    
    