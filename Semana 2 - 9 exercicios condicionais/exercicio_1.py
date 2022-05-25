# Considere as variáveis abaixo, inicializadas como segue:
# a) numero1 = 300
# b) numero2 = 100
# c) numero3 = 5
# d) string1 = "Rinoceronte"
# e) string2 = "Zebra"
# f) string3 = "bug”
# Para cada uma das seguintes expressões booleanas, classifique-a como
# Verdadeira, Falsa ou Ilegal.
# ● numero1 == numero3
# ● numero1 > numero3
# ● numero2 < numero3
# ● numero1 == string1
# ● numero1 == "Um"
# ● numero1 == "Trezentos"
# ● numero1 == "300"
# ● string2 == "Dois"
# ● string1 == "Rinoceronte"
# ● string3 != "Rinoceronte"
# ● string3 != "Rinoceronte" or numero1 > 1000
# ● numero2 <= numero1 / 3
# ● numero1 >= 200
# ● numero1 >= numero2 + numero3
# ● numero1 > numero2 and numero1 < numero3
# ● numero1 == 100 or numero1 > numero3
# ● numero1 < 10 or numero3 > 10
# ● numero1 == 30 and numero2 == 100 or numero3 == 100
numero1 = 300
numero2 = 100
numero3 = 5
string1 = 'Rinoceronte'
string2 = 'Zebra'
string3 = 'bug'

print(bool(numero1 == numero3))
print(bool(numero1 > numero3))
print(bool(numero2 < numero3))
print(bool(numero1 == string1))
print(bool(numero1 == "Um"))
print(bool(numero1 == "Trezentos"))
print(bool(numero1 == "300"))
print(bool(string2 == "Dois"))
print(bool(string1 == "Rinoceronte"))
print(bool(string3 != "Rinoceronte"))
print(bool(string3 != "Rinoceronte" or numero1 > 1000))
print(bool(numero2 <= numero1 / 3))
print(bool(numero1 >= 200))
print(bool(numero1 >= numero2 + numero3))
print(bool(numero1 > numero2 and numero1 < numero3))
print(bool(numero1 == 100 or numero1 > numero3))
print(bool(numero1 < 10 or numero3 > 10))
print(bool(numero1 == 30 and numero2 == 100 or numero3 == 100))