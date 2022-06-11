# Ler um número inteiro (assuma até três dígitos) e imprimir a saída da seguinte forma:
# CENTENA = x DEZENA = x UNIDADE = x
# Exemplo: 357 tem 3 centenas, 5 dezenas e 7 unidades.
num_inteiro = int(input('Informe o numero de 3 digitos: '))
uni = num_inteiro // 1 % 10
dez = num_inteiro // 10 % 10
cent = num_inteiro // 100 % 10
print('{} Centenas, {} Dezenas e, {} Unidades'.format((cent),(dez),(uni)))