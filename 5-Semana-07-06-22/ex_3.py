# Modifique o programa anterior para que utilize apenas uma lista e em cada posição da lista armazene um dicionário com o nome e a média
alunosAprovados = []

alunosEnotas = []

for i in range(5):

    nome = input('Informe seu nome: ')
    nota1 = float(input('Informe sua primeira nota: '))
    nota2 = float(input('Informe sua segunda nota: '))

    media = (nota1 + nota2) / 2

    aluno = {'Nome': nome, 'Média': media}
    alunosEnotas.append(aluno)

    if media >= 7:
        alunosAprovados.append(aluno)
       

print(f'Os alunos aprovados são: {alunosAprovados}')

os.system('clear')