# Crieumaclasseparaimplementarumacontacorrente.Aclasse
# deve  possuir  os  seguintes  atributos:
# a)número  da  conta
# b)nome  do  correntista
# c)saldo

# Os métodos são os seguintes:

# a)alterar_nome
# b)deposito
# c)saque

# No construtor,o saldo é opcional,com valor padrão zero e os demais atributos são obrigatórios

from Class import Conta_corrente

conta = Conta_corrente('124', 'Fernando')
print(conta.nome)
print(conta.saldo)

conta.alterar_nome('Luana')
print(conta.nome)
conta.deposito(1000)
print(conta.saldo)

conta.saque(750)
print(conta.saldo)

conta.saque(1000)



    