#Exercício 3 ficha 03

def main():
    
    num1 = float(input('1º número: '))
    num2 = float(input('2º número: '))
    
    maximo = max(num1, num2)
    print('Máximo: {:.2f}'.format(maximo))
    

def max(n1, n2):

    if n1 > n2:
        maior = n1
    else: 
        maior = n2
    
    return maior

main()