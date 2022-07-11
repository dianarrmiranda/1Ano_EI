

M,Q = 0,1

def cargoQuantidade(t,m):
    num =0
    for tupl in t:
        if tupl[0]==m:
            num +=tupl[1]
    return num

 

def unload(t, m, q):
    num = cargoQuantidade(t,m)
    if num < q:
        for i in range(len(t)-1,-1,-1):
            if t[i][0]==m:
                t.pop(i)
        return q-num
    else:
        for i in range(len(t)-1,-1,-1):
            if t[i][0] ==m:
                temp = t[i][1]
                t[i][1]-=q
                if t[i][1]<=0:
                    q-=temp
                    t.pop(i)
                else:
                    break
        return cargoQuantidade(t,m)
def main():
    t =[['coal',30],['rice', 50],['iron', 5], ['rice',42], ['coal',45]]
    
    print("t:",t)
    q=unload(t,'rice',40)
    print("unload(t,'rice',40) ->",q)
    print("t:",t)
    q=unload(t,'coal',50)
    print("unload(t,'coal',50) ->",q)
    print("t:",t)
    q=unload(t,'iron',20)
    print("unload(t,'iron',20) ->",q)
    print("t:",t)

if __name__ == "__main__":
    main()
