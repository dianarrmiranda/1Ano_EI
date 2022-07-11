import bisect
from re import A
file = "wordlist.txt"

with open(file, "r", encoding="latin-1") as text:
    lst=[]
    for i in text:
        word = i.strip()
        lst.append(word)

prefixo = ""
carac = input("insira um caracter ")
while (carac != ""):
	prox = prefixo+(chr(ord(carac)+1))
	prefixo += carac
	pos1 = bisect.bisect_left(lst, prefixo, 0, len(lst))
	pos2 = bisect.bisect_left(lst, prox, 0, len(lst))
	lwords = lst[pos1:pos2]

	if len(lwords)==1:
		print("Palavra encontrada:",lwords[0])
		break
	print(lwords)
	print("Prefixo atual:",prefixo)
	carac = input("Insira um novo caracter ")
	
print("Fim de programa")