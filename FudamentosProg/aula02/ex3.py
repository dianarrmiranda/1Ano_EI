#Exercício 3 ficha 02

x1 = float(input("number? "))
x2 = float(input("number? "))
x3 = float(input("number? "))

# Use conditional statements instead of max function!
if x3 < x1 > x2:
    m = x1
elif x3 < x2 > x1:
    m = x2
else:
    m = x3
    

print('Máximo: {}'.format(m))
