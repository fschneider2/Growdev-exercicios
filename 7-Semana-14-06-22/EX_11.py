# Utilize as seguintes faixas etárias nos exercícios em que for necessário.
# ● Jovens, 18 a 25 anos
# ● Adultos, 26 a 59 anos
# ● Idosos, igual ou maior que 60 anos

# Qual opção de pagamento é mais utilizada em cada faixa etária?

import os
os.system('clear')

from funcoes import importar_arquivo, dicionario_e_int

dados = importar_arquivo()
info = dicionario_e_int(dados)

jovens_c = 0
jovens_d = 0
jovens_din = 0
adultos_c = 0
adultos_d = 0
adultos_din = 0
idosos_d = 0
idosos_c = 0
idosos_din = 0

for i in info:

    if i['idade'] <= 25:
        if i['pagamento'] == 'credito':
            jovens_c += 1
        elif i['pagamento'] == 'debito':
            jovens_d += 1
        else:
            jovens_din += 1
        
    elif i['idade'] <= 59:
        if i['pagamento'] == 'credito':
            adultos_c += 1
        elif i['pagamento'] == 'debito':
            adultos_d += 1
        else:
            adultos_din += 1

    else:
        if i['pagamento'] == 'credito':
            idosos_c += 1
        elif i['pagamento'] == 'debito':
            idosos_d += 1
        else:
            idosos_din += 1
            
if jovens_c > jovens_d and jovens_c > jovens_din:
    mensagem = f'| Jovens utilizaram o credito em {jovens_c} sendo essa a forma de pagamento mais utilizada | '
elif jovens_d > jovens_c and jovens_d > jovens_din:
    mensagem = f'| Jovens utilizaram o débito em {jovens_d} sendo essa a forma de pagamento mais utilizada | '
else:
    mensagem = f'| Jovens utilizaram o dinheiro em {jovens_din} sendo essa a forma de pagamento mais utilizada | '

if adultos_c > adultos_d and adultos_c > adultos_din:
    mensagem += f'\n| Adultos utilizaram o credito em {adultos_c} sendo essa a forma de pagamento mais utilizada | '
elif adultos_d > adultos_c and adultos_d > adultos_din:
    mensagem += f'\n| Adultos utilizaram o débito em {adultos_d} sendo essa a forma de pagamento mais utilizada | '
else:
    mensagem += f'\n| Adultos utilizaram o dinheiro em {adultos_din} sendo essa a forma de pagamento mais utilizada | '    

if idosos_c > idosos_d and idosos_c > idosos_din:
    mensagem += f'\n| Idosos utilizaram o credito em {idosos_c} sendo essa a forma de pagamento mais utilizada | '
elif idosos_d > idosos_c and idosos_d > idosos_din:
    mensagem += f'\n| Idosos utilizaram o débito em {idosos_d} sendo essa a forma de pagamento mais utilizada   | '
else:
    mensagem += f'\n| Idosos utilizaram o dinheiro em {idosos_din} sendo essa a forma de pagamento mais utilizada | '

print('+','-'*82,'+')
print(mensagem)
print('+','-'*82,'+')