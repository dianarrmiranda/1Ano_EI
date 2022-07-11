def names():
    f = open('names.txt', 'r')
    dic = {}
    for nomes in f:
        nomes = nomes.split()
        lname= nomes[-1].strip()
        fname = nomes[0].strip()
        if lname not in dic:
            dic[lname] = set()
        dic[lname].add(fname)
    
    for i in dic:
        print(i,':', dic[i])

print(names())