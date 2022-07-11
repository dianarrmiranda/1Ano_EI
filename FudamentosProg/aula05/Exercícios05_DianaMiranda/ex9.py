#Exercício 9 Ficha 05

def evenThenOdd(s):
    return s[0::2] + s[1::2]

def removeAdjacentDuplicates(s):
    lst = []
    for i in s:
        lst.append(i)
    while True:
        prev_lst = lst[:]
        i = 1
        while i < len(lst):
            if lst[i - 1] == lst[i]:
                lst.pop(i)
            i += 1
        if prev_lst == lst:
            break
    s = ""
    s = s.join(lst)
    return s

def reapeatNumTimes(n):
    lst = []
    for i in range(1, n+1):
        for y in range(i):
            lst.append(i)
    return lst
    
def positionOfFirstLargest(lst):
    index = 0
    index_max = 0
    maxi = lst[0]
    for c in lst:
        index += 1
        if c > maxi:
            maxi = c
            index_max = index
    return index_max

def main():
    palavra = input('Palavra: ')
    print('Resultado: ', evenThenOdd(palavra))
    print('Resultado: ', removeAdjacentDuplicates(palavra))
    numero = int(input('Numero: '))
    print('Resultado: ', reapeatNumTimes(numero))
    
    lstd = []
    while True:
        valor = input("Valor: ")
        if valor == "":
            break
        n = str(valor)
        lstd.append(n)
    print('Resultado: ', positionOfFirstLargest(lstd))

main()