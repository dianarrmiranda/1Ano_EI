#Exercício 5 ficha 03

def main ():
    
    r = float(input('Número: '))
    
    res = resultado(r)
    
    print('tax({}) = {}'.format(r, res))
    
def resultado(num):
    if num <= 1000:
        return 0.1*num
    elif 1000 < num <= 2000:
        return 0.2*num - 100
    else:
        return 0.3*num-300

main()