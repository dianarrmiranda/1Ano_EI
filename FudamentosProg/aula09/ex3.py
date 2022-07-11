def mediana(lst):
    lst = sorted(lst)
    if len(lst)%2 == 0:
        med = len(lst)//2
        mediana = (lst[med-1] + lst[med])/2
    else:
        med = len(lst)//2
        mediana = lst[med]
    return lst, mediana
        
print(mediana([1,56,34,23,75,3,4,5,1]))
print(mediana([1,2,3,4,5,6,7,8,9,10,11,12]))
print(mediana([10,50,34,2,1,4,5,6,7]))