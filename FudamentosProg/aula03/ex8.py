#Exercício 8 ficha 03

def main():
    hora = float(input('Horas: '))
    minu = float(input('Minutos: '))
    seg = float(input('Segundos: '))
    
    s = hms2sec(hora, minu, seg)
    
    print('{:.0f}:{:.0f}:{:.0f} são {} segundos.'.format(hora,minu,seg,s))

def hms2sec(h, m, s):
    sec = float(h)*3600 + float(m) * 60 + float(s)
    return sec


main()