#Exercício 4 Ficha 05

def telToName(tel, telList, nameList):
    name = tel
    for t in telList:
        if t == tel:
            name = nameList[telList.index(t)]
    ...
    return name

def nameToTels(partName, telList, nameList):
    tels = []
    for n in nameList:
        if partName in n:
            tels.append(telList[nameList.index(n)])
    return tels

def main():
    telList = ['975318642', '234000111', '777888333', '911911911']
    nameList = ['Angelina', 'Brad',      'Claudia',   'Bruna']

    tel = input("Tel number? ")
    print( telToName(tel, telList, nameList) )
    #print( telToName('234000111', telList, nameList) == "Brad" )
    #print( telToName('222333444', telList, nameList) == "222333444" )

    name = input("Name? ")
    print( nameToTels(name, telList, nameList))
    #print( nameToTels('Clau', telList, nameList) == ['777888333'] )
    #print( nameToTels('Br', telList, nameList) == ['234000111', '911911911'] )


main()