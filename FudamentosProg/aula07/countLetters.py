
file = "pg3333.txt"

with open(file, "r", encoding="latin-1") as text:
        d = {}
        char = text.read(1)
        while char:
            if char.isalpha():
                char = char.lower()
                d[char] = d.get(char, 0) + 1
            char = text.read(1)
for e in sorted(d):
    print(e, d[e])

                        
        