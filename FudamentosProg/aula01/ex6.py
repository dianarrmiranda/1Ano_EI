#Exercício 6 ficha 01

import math

a = float(input('A? '))
b = float(input('B? '))

#Calcular hipotenusa
c = math.hypot(a,b)

#calcular sin
s = b/c

x = math.sin(s)

print('A hipotenusa é {:.2f}.'.format(c))
print('O ângulo é {:.2f}º.'.format(math.degrees(x)))

