# Em uma eleição presidencial existem quatro candidatos. Os votos são
# informados através de códigos. Os dados utilizados para a contagem dos
# votos obedecem à seguinte codificação:
# a) 1,2,3,4 = voto para os respectivos candidatos
# b) 5 = voto nulo
# c) 6 = voto em branco;

# Elabore um programa que leia o código de votação de 5 eleitores. Calcule
# e escreva:
# a) total de votos para cada candidato
# b) total de votos nulos
# c) total de votos em branco

listaCandidato1 = []
listaCandidato2 = []
listaCandidato3 = []
listaCandidato4 = []
listaNulo = []
listaBranco = []
contador = 1

while contador <= 5:
    voto = int(input('Informe 1 para o Candidato Zeze. \nInforme 2 para o candidato Lele.'
        '\nInforme 3 para a candidata Juju. \nInforme 4 para a candidata Lulu.\nInforme 5 para votar nulo.' 
           '\nInforme 6 para votar em branco. \n------------------------------------ \nInforme seu voto: '))  

    while voto < 1 or voto > 6:
        int(input('Informe 1 para o Candidato Zeze. \nInforme 2 para o candidato Lele.'
        '\nInforme 3 para a candidata Juju. \nInforme 4 para a candidata Lulu.\nInforme 5 para votar nulo.' 
           '\nInforme 6 para votar em branco.\n------------------------------------ \nInforme seu voto: '))

    if voto == 1:
        listaCandidato1.append(voto)
    elif voto == 2:
        listaCandidato2.append(voto)
    elif voto == 3:
        listaCandidato3.append(voto)
    elif voto == 4: 
        listaCandidato4.append(voto)
    elif voto == 5:
        listaNulo.append(voto) 
    else:
        listaBranco.append(voto)
    contador += 1


print(f'Candidato Zeze = {len(listaCandidato1)} votos')   
print(f'Candidato Lele = {len(listaCandidato2)} votos')   
print(f'Candidata Juju = {len(listaCandidato3)} votos')   
print(f'Candidato Lulu = {len(listaCandidato4)} votos')   
print(f'Votos Nulos = {len(listaNulo)} votos')   
print(f'Votos Branco = {len(listaBranco)} votos')   


