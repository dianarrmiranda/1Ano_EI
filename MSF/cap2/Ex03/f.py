#f) Repita a alínea anterior, com um passo 10 vezes menor

import numpy as np
import matplotlib.pyplot as plt

#Alinea e

t0 = 0 #s
tf = 3 #s
g = 9.8 #m/s g = aceleracao

dt = 0.05 #s

n = int((tf-t0)/dt)

t = np.linspace(0,3,n)
v = np.empty(n)
v0 = v[0]
y = np.empty(n)
y0 = y[0]

for i in range(n-1):
    v[i+1] = v[i] + g * dt
    y[i+1] = y[i] + v[i]*dt
    

plt.plot(t,y, label= "y(t) do objeto")
plt.xlabel('t (s)')
plt.ylabel('y posição (m)')
plt.title("Gráfico da posição y(t) de 0 a 3.0 s (Método de Euler)")

for i in range(n-1):
    if (t[i]>(2-dt) and t[i+1] <(2+dt)):
        print("dt, t, y = ", dt, t[i+1], y[i+1])
        print("A posição em 2s é {:.1f} m".format(y[i+1]))
        plt.plot(t[i+1],y[i+1], "o", label="v(t) em 2s")
        break

plt.legend()
plt.show()