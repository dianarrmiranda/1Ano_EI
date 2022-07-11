#Exercício 11 ficha 03

n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))


def mdc(m,n):
    if m == 0 or n ==0:
        print('ERRO!')
    else:
        m,n = max(m,n), min(m,n)
    
        while m%n != 0:
            n = m%n
            m = n
        return n
    
x = mdc(n1,n2)
 
print(x)