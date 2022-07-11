
def loadFile(fname, lst):
    with open(fname, "r") as f:
        f.readline()
        for line in f:
            linha = line.split('\n')
            l = line.split('\t')
            nova = (int(l[0]), l[1], float(l[5]),float(l[6]),float(l[7]))
            lst.append(nova)
       
    return lst

# b) Crie a função notaFinal aqui...
def notafinal(reg):
    
    nota1 = reg[2]
    nota2 = reg[3]
    nota3 = reg[4]
    
    media = (nota1 + nota2 + nota3) / 3
    
    return media
    

# c) Crie a função printPauta aqui...
def printPauta(lst, new_file):
    with open(new_file, 'w') as pauta_file:
        print('{:7s}{:^60s}{:>5s}'.format('Número', 'Nome', 'Nota'),file=pauta_file)
        for l in lst:
            print('{:7d}{:^60s}{:.2f}'.format(l[0], l[1], notafinal(l)), file=pauta_file)

# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    # ordenar a lista
    lst.sort()
    
    # mostrar a pauta
    printPauta(lst, "Pauta.txt")



# Call main function
if __name__ == "__main__":
    main()