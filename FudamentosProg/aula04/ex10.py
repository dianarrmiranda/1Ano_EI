#Exercício 10 ficha 04

#def isprime(n):
numero = 1
divisores = 0

def isprime(numero):
    divisores = 0
    for i in range(1, numero): #o próprio número não está na lista
        if numero % i == 0: #condição para verificar se o número tem algum divisor
            divisores += 1 #se tiver algum divisor, o numero de divisor passa de 0 a 1, se a condição não se verificar, não tem divisor
            if divisores > 1: 
                break
    if divisores > 1:
        print(numero, "não é primo")
    else:
        print(numero, "é primo")
while numero <= 100:
    isprime(numero)
    numero += 1