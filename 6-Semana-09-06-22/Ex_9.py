# O que faz a função abaixo se passarmos os valores 5 e 1 respectivamente para os parâmetros n e res.

def fat(n, res):
if n==0:
return res
res = res * n
return fat(n - 1, res)