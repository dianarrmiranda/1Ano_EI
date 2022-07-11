#Exercício 05 ficha 04

import random

def main():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101);
    print("Can you guess my secret?")
    num = int(input("Número:"))
    
    # put your code here
    print("Acertou depois de {} tentativas".format(advinha(secret,num)))

def advinha(n, numero):
    x=1
    while numero != n:
        if numero > n:
            print("High")
        else:
            print("Low")
        numero = int(input("Nova tentativa:"))
        x+=1
    return x

main()
