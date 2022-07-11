
file = "pg3333.txt"

with open(file, "r", encoding="latin-1") as text:
        d = {}
        char = text.read(1)
        while char:
            if char.isalpha():
                char = char.lower()
                d[char] = d.get(char, 0) + 1
            char = text.read(1)
            
d = sorted(d.items(), key= lambda n: n[1], reverse=True)

for x in d:
	print(x)

print(d)

