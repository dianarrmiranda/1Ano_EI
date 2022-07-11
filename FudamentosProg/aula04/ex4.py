#Exercício 04 ficha 04

n = int(input("Número: "))

def factorial(n):
    nfact = n
    while n != 1:
        n -= 1
        nfact *= n
        
    return nfact
    
print(factorial(n))
