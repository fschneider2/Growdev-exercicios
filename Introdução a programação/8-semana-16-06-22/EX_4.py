# Crie uma classe que modele um Tamagochi (Bichinho Eletrônico):
# a)Atributos
# i)Nome
# ii)Fome
# iii)Saúde
# iv)Idade.
# b)Métodos
# i)alterar_nome,
# ii)alterar_fome
# iii)alterar_saude
# iv)alterar_idade
# v)retornar_nome
# vi)retornar_nome
# vii)retornar_saude
# viii)retornar_idade

from Class import Tamagochi

tamagochi = Tamagochi()

tamagochi.alterar_nome("Krug")
print(tamagochi.retornar_nome())

tamagochi.alterar_fome(4)
print(tamagochi.retornar_fome())

tamagochi.alterar_idade(15)
print(tamagochi.retornar_idade())

tamagochi.alterar_saude(3)
print(tamagochi.retornar_saude())
