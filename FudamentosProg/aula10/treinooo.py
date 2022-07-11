def reverse(n):
    
    if len(n) ==1:
        return n
    else:
        return n[-1] + reverse(n[:-1])   
        
def junta(n):
    n = n.lower()
    n = n.replace(",","")
    n = "".join(n.split())
    s = reverse(n)
    if s==n:
        return 'True'
    else:
        return 'False'

print(junta('DIAana miranda'))
print(junta('kayak'))
print(junta('Reviled did I, live, said I as evil I did deliver'))


def inv(lst,l):
    n = len(lst)
    if n < 1:
        return lst
    else:
        l.append(lst[-1]) 
        inv(lst[:-1],l)
    return l

def limp(lst):
    l =[]
    return inv(lst, l)
    

x=[1,2,3,4,5]
v=[1,10,45,4,5,70,53,1]
print(limp(x))

print(limp(v))