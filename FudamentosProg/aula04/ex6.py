#Exercício 06 ficha 04

termos = int(input('Número: '))

def leibniz(n):

    t_sum = 0
    
    for i in range(n):
        term = (-1)**i / (2*i+1)
        t_sum += term
        
    return t_sum*4

pi = leibniz(termos)

print(pi)
