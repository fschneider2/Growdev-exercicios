# A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.

n_esimo = int(input('Informe um número: '))
a1 = 0
a2 = 1
a3 = 0
lista_fibonacci = [1]

while a3 <= n_esimo:
    a3 = a1 + a2
    lista_fibonacci.append(a3)
    a1 = a2
    a2 = a3
print(lista_fibonacci)

    
    

