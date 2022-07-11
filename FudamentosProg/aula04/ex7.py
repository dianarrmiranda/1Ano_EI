#Exercício 07 ficha 04

tot = 0.0
n= 0
while True:
    s = input("valor? ")
    if s == "": break   # if empty line, stop repeating!
    v = float(s)
    tot = tot + v
    n+=1

media = tot/n

print('Média: {}'.format(media))

