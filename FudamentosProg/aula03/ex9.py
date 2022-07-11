#Exercício 9 ficha 03

def main():
    seg = float(input('Segundos: '))
    
    s = sec2hms(seg)
    
    print(s)

def sec2hms(s):
    h = s//3600
    rest = s % 3600
    m = rest // 60
    seg = rest%60
    
    f = print('{} segundos são {:.0f}:{:.0f}:{:.0f}'.format(s,h,m,seg))
    return f


main()