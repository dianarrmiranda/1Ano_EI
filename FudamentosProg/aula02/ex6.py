#Exercício 6 ficha 02

age = int(input("Age? "))

if age < 0:
    print("ERROR: invalid age!")
    exit(1)     # this terminates the program

print("Age:", age)

if age <= 13:
    cat = "child"
elif 13 < age < 20:
    cat = "teenager"
else:
    cat = "adult"

print("Category:", cat)