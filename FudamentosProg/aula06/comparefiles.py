#Exercício 6 ficha 06

def compareFiles(file1, file2):
    #Abrir os ficheiros em leitura binária
    file1 = open(file1, "rb")
    file2 = open(file2, "rb")
    
    #Definir a primeira porção dos ficheiros a comparar
    compara1 = file1.read(1024)
    compara2 = file2.read(1024)
    
    #Este while vai correr enquanto um dos compara for diferente de ""
    while compara1 or compara2:
        if compara1 != compara2:
            #Fechar os ficheiros antes do return
            file1.close()
            file2.close()
            return "Not equal"
            
        #Definir as próximas porções a ser comparadas
        compara1 = file1.read(1024)
        compara2 = file2.read(1024)
    
    #Se a instrução if nunca ocurreu, então os ficheiros são iguais
    #Fechar os ficheiros antes do return
    file1.close()
    file2.close()
    return "Equal"
    
print(compareFiles("nums.txt", "copia_nums.txt"))
print(compareFiles("nums.txt", "numeros6.txt"))