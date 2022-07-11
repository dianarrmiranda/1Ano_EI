def count(file):
    f = open(file,'r', encoding="latin-1")
    
    char = f.read(1)
    dic={}
    while char:
        if char.isalpha():
            char = char.lower()
            dic[char] = dic.get(char,0)+1
        char = f.read(1)
    
    
    for i in sorted(dic):
        print(i,dic[i])
    
        
        
        
x = count('pg3333.txt')