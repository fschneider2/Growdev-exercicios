# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.


lista = []

for i in range(10):
    vetor = float(input('Digite um número: '))
    lista.append(vetor)
 
listaInversa = list(reversed(lista))
    
print(f'Digitados: {lista}\n')

print(f'Inverso = {listaInversa}\n')

os.system('clear')