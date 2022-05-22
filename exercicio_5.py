# Escreva um programa que receba como entrada a quantidade de torcedores do time X, 
# do time Y e do time Z, calcula e exibe qual a porcentagem de torcedores de cada time..

time_x = int(input('Informe a quantidade de torcedores do time x: '))
time_y = int(input('Informe a quantidade de torcedores do time y: '))
time_z = int(input('Informe a quantidade de torcedores do time z: '))
total = time_x + time_y + time_z
porcent_x = (time_x * 100) / total
porcent_y = (time_y * 100) / total
porcent_z = (time_z * 100) / total
print('A torcida do time x representa, '+ str(porcent_x) + '% do publico total.')
print('A torcida do time y representa, '+ str(porcent_y) + '% do publico total.')
print('A torcida do time z representa, '+ str(porcent_z) + '% do publico total.')
