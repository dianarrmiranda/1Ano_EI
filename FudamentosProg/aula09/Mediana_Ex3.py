def mediana(lst):
    lstOrdenada = sorted(lst)
    print(lstOrdenada)
    
    if len(lstOrdenada)%2 == 0:
        n = int(len(lstOrdenada)/2)
        med = (lstOrdenada[n] + lstOrdenada[n-1])/2
    else:
        n=int(len(lstOrdenada)/2)
        med = lstOrdenada[n]
    return med
        

print(mediana([12,4,7,15,65,3]))
print(mediana([12,4,7,15,65,3,10]))