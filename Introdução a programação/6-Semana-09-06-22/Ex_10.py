# Implemente um programa onde o usuário deve adivinhar as letras de uma palavra por meio de palpites. A palavra deve ser mostrada inicialmente com
# as letras substituídas por underlines, conforme exemplo abaixo.

# dados    =>   _ _ _ _ _

# O usuário deve então palpitar sobre as letras que ele julga estarem na frase. 
# A cada letra que errar, ele perde 1 ponto. A cada letra que ele acertar a mesma deve ser exibida na tela, exemplo:

# Palpite: d
# Saída: d _ d _ _

# Se completar a frase o usuário ganha o jogo, se sua pontuação zerar ele perde o jogo. Ao iniciar o jogo, a pontuação é de 4 pontos.


# minha resposta é uma variação do enunciado, executei um codigo para realizar um jogo parecido com o do game termoo <https://term.ooo/>

import os
import random

os.system('clear')

palavras = ['FATOS','JOGOS','GANHA','BARCO']
palavras_usadas = []
chances = 5

palavra_escolhida = random.choice(palavras)

palavras.remove(palavra_escolhida)

palavras_usadas.append(palavra_escolhida)
if palavra_escolhida == palavras_usadas:
    palavra_escolhida = random.choice(palavras)


print(palavra_escolhida)
print(palavras)






# def analisar_palavra_usuario(a):
    