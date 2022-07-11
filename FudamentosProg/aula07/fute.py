
def allmatches(lst):
    jogos= []
    for team1 in lst:
        for team2 in lst:
            if team1 != team2:
                jogos.append((team1,team2))            
    return jogos

def results(jogos, tabela):
    dic = {}
    
    for i in jogos:
        print('No jogo {} vs {}. Qual foi o resultado? '.format(i[0], i[1]))
        resTeam1 = int(input('{} : '.format(i[0])))
        resTeam2 = int(input('{} : '.format(i[1])))
        
        dic[i] = (resTeam1, resTeam2)
        
        tabela[i[0]][3] += resTeam1
        tabela[i[0]][4] += resTeam2
        tabela[i[1]][3] += resTeam2
        tabela[i[1]][4] += resTeam1
        
        if resTeam1 > resTeam2:
            tabela[i[0]][0] += 1
            tabela[i[1]][2] += 1
            tabela[i[0]][5] += 3
        elif resTeam1 < resTeam2:
            tabela[i[0]][2] += 1
            tabela[i[1]][0] += 1
            tabela[i[1]][5] += 3
        else:
            tabela[i[0]][2] += 1
            tabela[i[1]][1] += 1
            tabela[i[1]][5] += 1
            tabela[i[0]][5] += 1
        
    return tabela

def campeoes(x):
    max=0
    for i in x:
        pontos = x[i][5]
        if pontos> max:
            max = pontos
            champ = i
    return champ
def main():
    equipas = []
    tabe={}
    while True:
        club = input("Equipa de futebol: ")
        if club == "":
            break
        n = str(club)
        equipas.append(n)
    x = allmatches(equipas)
    
    print('{:8} {:^8} {:8}'.format('','Jogos',''))
    for i in x:
        print('{:8} {:^8} {:8}'. format(i[0],'vs', i[1]))
    
    for equipa in equipas:
        tabe[equipa] = [0,0,0,0,0,0]
    
    result = results(x, tabe)
    camp = campeoes(result)
    
    print('{:8} {:8} {:8} {:8} {:8} {:8} {:8}'.format('Equipa','Vitórias','Empates','Derrotas', 'GM', 'GS', 'Pontos'))
    for i in result:
        print('{:8} {:8} {:8} {:8} {:8} {:8} {:8}'.format(i,result[i][0],result[i][1],result[i][2], result[i][3], result[i][4], result[i][5]))
    
    print('Campeao: ', camp)
    
main()