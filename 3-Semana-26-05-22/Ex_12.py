# Uma certa operadora de telefonia móvel cobra R$ 5,00 mensais pelo seu
# plano básico de transmissão de SMS (mensagens de texto), sendo que taxas
# adicionais são cobradas conforme as regras abaixo:
# a) As primeiras 60 mensagens estão incluídas no plano básico;

# b) b. Se o usuário mandar mais de 60 mensagens, cada mensagem
# adicional custará R$ 0.05, até o limite de 180 mensagens.
# c) c. Acima de 180 mensagens, o valor de cada uma delas passa a R$
# 0,10;
# d) d. A soma dos impostos estaduais e federais amonta a 12% do valor
# de cada fatura.
# Com base nessas informações, crie um algoritmo para ler o número total de
# mensagens enviadas por um usuário. Ao final, calcule o valor da conta e
# mostre todos os dados, incluindo o valor da conta com e sem impostos.

quantidade = int(input('Vamos calcular o total de sua conta, informe quantos SMS você enviou: '))

fixo = 5

unidade = 0

total = quantidade * unidade + fixo
if quantidade > 60 and quantidade <= 180:
    unidade = 0.05
    total = quantidade * unidade + fixo - 3.0
elif quantidade > 180:
    unidade = 0.10
    total = quantidade * unidade + fixo - 12

total_com_imposto = total / .88

custo_imposto = total_com_imposto - total

print('Você enviou {} SMS, irá pagar: R$ {:.5} | sendo R$ {:.4} referente ao serviço e R$ {:.4}'
                        ' de imposto.'.format(quantidade, total_com_imposto, total, custo_imposto,))