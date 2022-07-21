import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
from funcoes import importar_arquivo
import os

dados = importar_arquivo()

os.system('clear')

# a = organize uma tablema de frequência para as classes.

# labels = ['G1', 'G2', 'G3', 'G4', 'G5']
# men_means = [20, 34, 30, 35, 27]
# women_means = [25, 32, 34, 20, 25]

# x = np.arange(len(labels))  # the label locations
# width = 0.35  # the width of the bars

# fig, ax = plt.subplots()
# rects1 = ax.bar(x - width/2, men_means, width, label='Men')
# rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.set_xticks(x, labels)
# ax.legend()

# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, paddng=3)

# fig.tight_layout()

# plt.show()

# b = para cada semana, faça um gráfico de linha, para acompanhar a evolução da temperatura

# c =  calcule a média de toda a série.

temperatura = []

for i in dados:
    if i['temperatura'] != 0:
        temperatura.append(i['temperatura'])
print(temperatura)

media = sum(temperatura) / len(temperatura)

print('A média de toda a série é:: ', media)

# d = calcule a média para cada semana. 

# e = obter o box-plot para toda série e para cada semana.  