#Exercício 10 Ficha 02

import math as math
import numpy as np

print("Enter the coordinates in mm from the center of the board.")
x = float(input("x? "))
y = float(input("y? "))

# Points of the sectors, clockwise from the top
# Example: the sector right from the center is POINTS[5] == 6.
POINTS = (20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5)

# COMPLETE...

#Calcular raio
r = math.sqrt(math.pow(x,2) + math.pow(y,2))

#Calcular angulo em radianos
theta = np.arctan2(y,x)

#Angulo em graus
graus = 180*(theta/math.pi)

print(r)
print(theta)
print(graus)

#x**2 + y**2 < z


#if 2<=r:
#f =100
#elif 10<=r<=20:

#elif 40 <=r<=50:
#elif r>=60:
#else:

print(score)
