import bisect

file = "wordlist.txt"

with open(file, "r", encoding="latin-1") as text:
    lst=[]
    for i in text:
        word = i.strip()
        lst.append(word)
   

n = bisect.bisect_left(lst, "ea")
m = bisect.bisect_left(lst, "eb")
z = bisect.bisect_left(lst, "tb")

print(m-n,"words that start with 'ea'")
for x in range(n, m):
	print(lst[x])
	
print(z)
print(lst[z])
    