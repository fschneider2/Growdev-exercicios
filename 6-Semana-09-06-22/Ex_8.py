# Escreva uma função que conte o número de espaços em branco em uma frase passada como parâmetro.

import os

os.system('clear')

phrase = input('Digite uma frase: ')

def check_space(a):

    count = 0

    for i in phrase:
        if i == " ":
            count += 1
    letters = len(a) - count
    
    print(f'{phrase} possui: {count} espaços e {letters} letras')

check_space(phrase)