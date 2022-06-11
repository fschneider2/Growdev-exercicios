# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos
# elementos intercalados dos dois outros vetores.
import itertools 
import os

os.system('clear')

vetor1 = []
vetor2 = []
vetor3 = []


for i in range (0, 20, 2):
    vetor1.append(i)

for a in range(1, 20, 2):
    vetor2.append(a)

# para juntar, utilizei o itertools. Neste caso poderia ter utilizado a função .sorted, mas como a ideia era intercalar elementos, e estes poderiam 
# não ser em sequencia, utilizei o *zip. Anotação para eu mesmo:  se usar so o zip, sem o: *, o resultado é (1,2), (3,4),.........
vetor3 = list(itertools.chain(*zip(vetor1, vetor2)))

print(vetor1)
print(vetor2)
print(vetor3)

# poderia ser utilizado o random, para criar os dois vetores...

# vetor1 = random.sample(range(100), 10)

# # Criei o vetor 2 desta forma, para que os elementos fiquem negativos, e mais facil de identificar os elementos intercalados no vetor 3.
# while contador <= 10:
#     i = random.randint(-100, 0)
#     vetor2.append(i)
#     contador += 1



