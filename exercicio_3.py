# Elaborar um programa que calcule e apresente o valor do volume de uma
# caixa retangular, utilizando a fórmula.
# 𝑉𝑂𝐿𝑈𝑀𝐸 = 𝐶𝑂𝑀𝑃𝑅𝐼𝑀𝐸𝑁𝑇𝑂 * 𝐿𝐴𝑅𝐺𝑈𝑅𝐴 * 𝐴𝐿𝑇𝑈𝑅A
texto = ('Olá, vou te ajudar a calcular o volume de uma caixa retangular!')
print(texto)
comprimento = float(input('Informe o comprimento em cm: '))
largura = float(input('Informe a largura em cm: '))
altura = float(input('Informe a altura cm: '))
volume = comprimento * largura * altura
print('O volume da caixa retangular é: '+ str(volume))
