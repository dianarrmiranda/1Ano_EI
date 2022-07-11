#Exercício 4 ficha 03

def main():
    
    num1 = float(input('1º número: '))
    num2 = float(input('2º número: '))
    num3 = float(input('3º número: '))
    
    maximo = maxx(num1, num2)
    maximo3 = max3(num1, num2, num3)
    print('Máximo: {:.2f}'.format(maximo3))
    

def maxx(n1, n2):

    if n1 > n2:
        maior = n1
    else: 
        maior = n2
    
    return maior
    

def max3(n1, n2, n3):
    
    if n3 > maxx(n1, n2):
        maior = n3
    else:
        maior = maxx(n1, n2)
    return maior
    
main()

