# Escreva um programa que aceite uma quantidade de minutos e o converta em horas e dias. 
# Por exemplo, 6.000 minutos equivalem a 100 horas e é igual a 4.167 dias.
min_informados = int(input('Informe a quantidade de minutos, que irei converter em horas e dias: '))
min_horas = min_informados / 60
min_dias = min_horas / 24
print(min_informados,'minutos, equivalem à:',round(min_horas, 2),'horas e:',round(min_dias, 2),'dias.')
