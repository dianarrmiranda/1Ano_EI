#Exercício 2 ficha 03

def main():
    p = int(input('Número: '))
    
    resultado = conta(p)
    
    print('P({}) = {}'.format(p, resultado))


def conta(num):
    return num**2+2*num+3

main()