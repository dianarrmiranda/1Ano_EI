def allMatches(lstequipas):
    jogos = []
    for equipa1 in lstequipas:
        for equipa2 in lstequipas:
            if equipa1 != equipa2:
                jogos.append((equipa1, equipa2))
    return jogos
    
def printTabela(dic):
    print("{:10} | {} | {} | {} | {} | {} | {}".format("Equipa", "Vitórias", "Empates", "Derrotas", "Golos Marcados", "Golos Sofridos", "Pontos"))
    for team in dic:
        print("{:10} | {:^8} | {:^7} | {:^8} | {:^14} | {:^14} | {:^6}".format(team, dic[team][0], dic[team][1], dic[team][2], dic[team][3], dic[team][4], dic[team][5]))
        
def setEquipas():
    Equipas=[]
    print("Introduza uma equipa de cada vez, ou uma linha em branco para terminar.")
    while True:
        equipa=input()
        if equipa == "":
            break
        else:
            Equipas.append(equipa)
    return Equipas

def setCampeao(dic):
    campeao = list(dic)[0]
    for equipa in dic:
        if dic[equipa][5] > dic[campeao][5]:
            campeao = equipa
        elif dic[equipa][5] == dic[campeao][5] and dic[equipa][3] - dic[equipa][4] > dic[campeao][3]-dic[campeao][4]:
            campeao = equipa
    return campeao


Equipas = setEquipas()
jogos = allMatches(Equipas)
resultados = {}
tabela = {}

for equipa in Equipas:
    #vitórias, empates, derrotas, golos marcados, golos sofridos, pontos
    tabela[equipa] = [0,0,0,0,0,0]

for jogo in jogos:
    print()
    print("Resultado do Jogo ", jogo, "? ")
    x = int(input("{} : ".format(jogo[0])))
    y = int(input("{} : ".format(jogo[1])))
    
    resultados[jogo] = (x, y)
    
    tabela[jogo[0]][3] += x
    tabela[jogo[0]][4] += y
    tabela[jogo[1]][3] += y
    tabela[jogo[1]][4] += x
    
    if x>y:
        tabela[jogo[0]][0] += 1
        tabela[jogo[0]][5] += 3
        tabela[jogo[1]][2] += 1
    elif x<y:
        tabela[jogo[1]][0] += 1
        tabela[jogo[1]][5] += 3
        tabela[jogo[0]][2] += 1
    else:
        tabela[jogo[0]][1] += 1
        tabela[jogo[1]][1] += 1
        tabela[jogo[0]][5] += 1
        tabela[jogo[1]][5] += 1

print()
printTabela(tabela)
print()
print("A equipa vencedora é: ", setCampeao(tabela))