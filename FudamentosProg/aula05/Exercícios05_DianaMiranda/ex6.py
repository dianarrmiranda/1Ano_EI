#Exercício 6 Ficha 05

def countdigits(frase):
    n = 0
    for c in frase:
        if c.isdigit():
            n += 1
    return n
    
def main():
    f = input('Frase: ')

    print("result: ", countdigits(f))    
        

main()
