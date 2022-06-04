# Faça um programa que leia um valor N e mostre os N termos da Série a
# seguir:
# a) S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m

soma = 0
valorN = int(input('Informe um número: '))
m = 1
# iniciei exibindo o 'S =' seguido da expressão end='', nesse caso, siguinifica que o print tera continuação
print('S = ', end='')
for i in range(1, valorN + 1):
    print(f'{i}/{m}', end='') # continuando o mesmo print, add so a formula 1/1....
    if i < valorN:
        print(' + ', end='') # enquanto o valor de i for menor que o numero informado, ele vai dando o sinal de + 1/1 + 1/2....
    else:
        print('.') # se não, ponto final, acabou essa parte.
    
    soma += i / m # fiquei em duvida se era necessario, fiz igual.
    m += 2
print(f"A soma da série é: {soma:.2f}")

 
