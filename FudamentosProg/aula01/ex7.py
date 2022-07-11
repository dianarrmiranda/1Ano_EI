#Exercício 7 ficha 01

# This program reads the coordinates of two points (x1,y1) and (x2,y2).

x1 = float(input("x1? "))
y1 = float(input("y1? "))
x2 = float(input("x2? "))
y2 = float(input("y2? "))

# Find and print the distance between the points!
# ...
import math

d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print('A distânccia entre os pontos são {:.2f}'.format(d))

