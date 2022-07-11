#Exercício 8 Ficha 05

def ispalindrome(s):
    p=""
    if str(s) == str(s)[::-1] :
        p = True
    else:
        p = False
    return p

def main():
    palavra = input('String: ')
    print(ispalindrome(palavra))
    
main()