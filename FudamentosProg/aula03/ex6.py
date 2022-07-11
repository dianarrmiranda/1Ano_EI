#Exercício 6 ficha 03

def main():
    
    a1 = float(input('a1 = '))
    b1 = float(input('b1 = '))
    a2 = float(input('a2 = '))
    b2 = float(input('b2 = '))
    
    r =intersects(a1,b1,a2,b2)
    
    print(r)
    
def intersects(a1, b1, a2, b2):
    
    if a1>=b1 or a2>=b2:
        return 'Erro!!'
    elif (a1 < a2 < b1) or (a1 < b2 < b1):
        return 'True'
    else:
        return 'False'

main()