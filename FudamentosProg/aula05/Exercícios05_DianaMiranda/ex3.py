#Exercício 3 Ficha 05


def inputFloatList():
    lst = []
    while True:
        num = input("Número? (vazio para terminar): ")
        if num == "":
            break
        n = float(num)
        lst.append(n)
    return lst

def countLower(lst, v):
    inf = []
    for n in lst:
        if n < v:
            inf.append(n)
    return inf, len(inf)

def minmax(lst):
    if lst == []:
        return "none"
    minin = lst[0]
    maxi = lst[0]
    for n in lst:
        if n > maxi:
            maxi = n
        if n < minin:
            minin = n
    return minin, maxi

def main():
    lst = inputFloatList()
    avg = (minmax(lst)[0] + minmax(lst)[1]) / 2 
    low = countLower(lst, avg)

    print("A média entre o mínimo e máximo é", avg)
    print(" {} números {} são inferiores à média".format(low[1], low[0]))


main()
