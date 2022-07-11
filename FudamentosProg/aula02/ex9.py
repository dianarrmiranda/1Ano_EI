#Exercício 9 ficha 02

CTP = float(input('Nota CTP: '))
CP = float(input('Nota CP: '))


NF = (0.36 * CTP) + (0.64 * CP)

if CP > 6.5 and CTP > 6.5:
    if NF >= 9.5:
    
        print('Nota Final: {:.0f}'.format(NF))
    
    else:
        ATPR = float(input('Nota ATPR: '))
        APR = float(input('Nota APR: '))
    
        maxT = max(ATPR, CTP)
        maxP = max(APR, CP)
    
        NR = (0.36 * maxT) + (0.64 * maxP)
    
        print('Nota Final Recurso: {:.0f}'.format(NR))
    
else:
    print('Nota Final: Código 66')