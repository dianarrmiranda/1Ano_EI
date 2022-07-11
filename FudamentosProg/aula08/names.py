d={}

with open("names.txt", "r") as file:
    file.readline()
    for line in file:
        nomes = line.split()
        lname = nomes[-1].strip()
        fname=nomes[0]
        if lname not in d:
            d[lname] = set()
        d[lname].add(fname)
      

for x,y in d.items():
    print(x, " : ", y)
            
