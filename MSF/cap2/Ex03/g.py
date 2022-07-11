#g) Compare o resultado obtido em e) e f) com o resultado exato. Que conclui?

import numpy as np
import matplotlib.pyplot as plt

t0 = 0 #s
tf = 4 #s
g = 9.8 #m/s g = aceleracao

dt = 0.001 #s

n = int((tf-t0)/dt)

t = np.linspace(0,3,n)
v = np.empty(n)
v0 = v[0]
y = np.empty(n)
y0 = y[0]



#Alinea g - Quanto menor o dt for, maior a aproximação do método de euler do valor analítico.

y2 = y0 + v0*2 + (1/2)*g*(2**2)

print("Com dt=0.5 temos y(2) = 14.7 m")
print("Com dt=0.05 temos y(2) = 19.1 m", )
print("O resultado exato é {:.1f} m".format(y2))