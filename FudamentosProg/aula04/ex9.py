#Exercício 09 ficha 04

def fibonacci(n):
    if n == 0:
        res = 0
    elif n==1 or n==2:
        res = 1
    else:
        F0 = 0
        F1 = 1
        for i in range(n-2):
            res = F0 + F1
            F0 = F1
            F1 = res
        return res

#fn      fn1   + fn2
#fib 2 = fib 1 + fib 0
#fib 3 = fib 2 + fib 1
#fib 4 = fib 3 + fib 2

def main():
    num = int(input('Número. '))
    
    resultado = fibonacci(num)
    
    print(resultado)
    
main()