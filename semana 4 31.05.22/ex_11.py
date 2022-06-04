# Supondo que a população de um país A seja da ordem de 80000 habitantes
# com uma taxa anual de crescimento de 3% e que a população de B seja
# 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um
# programa que calcule e escreva o número de anos necessários para que a
# população do país A ultrapasse ou iguale a população do país B, mantidas as
# taxas de crescimento.

contador = 0
paisA = 80000
paisB = 200000

while paisA <= paisB:
    paisA = paisA * 0.03 + paisA
    paisB = paisB * 0.015 + paisB
    contador += 1

print(f'O país A vai levar {contador} anos para ser maior que o País B')