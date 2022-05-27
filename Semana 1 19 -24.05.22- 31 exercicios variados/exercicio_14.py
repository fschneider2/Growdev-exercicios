# Escreva um programa que leia dois números e faça a adição, subtração, divisão e 
# multiplicação dos dois números, e após, exiba os 4 resultados calculados.
class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def soma(self):
        return self.a + self.b

    def multi(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def sub(self):
        return self.a - self.b
calculadora = Calculadora(10, 2)
print(calculadora.soma())
print(calculadora.sub())
print(calculadora.div())
print(calculadora.multi())