#Exercício 5 Ficha 05


def allMatches(lstequipas):
    jogos = []
    for equipa1 in lstequipas:
        for equipa2 in lstequipas:
            if equipa1 != equipa2:
                jogos.append((equipa1, equipa2))
    return jogos
    

def main():
    equipas = []
    while True:
        club = input("Equipa de futebol: ")
        if club == "":
            break
        n = str(club)
        equipas.append(n)
    
    print(allMatches(equipas))
main()