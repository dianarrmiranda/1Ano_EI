#Exercício 7 Ficha 05

def Maiuscula(frase):
    n=""
    for c in frase:
        if c.isupper():
            n = n + c
    return n

    
def main():
    f = input('Frase: ')

    print("result: ", Maiuscula(f))    
        

main()
