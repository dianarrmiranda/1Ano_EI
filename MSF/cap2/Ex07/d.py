#d) Resolva as alíneas anteriores, considerando a resistência do ar. Resolva usando o
#método de Euler. A velocidade terminal da bola no ar é de 100 km/h. 

import matplotlib.pyplot as plt
import numpy as np

vi = 10 # m/s
dt = 0.001
g = 9.8
t0 = 0
tf = 2.2+dt
vt = 27.7778 # VElocidade terminal - 100 km/ hour = 27.7778 m/s
D = g/vt**2 

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)
v = np.empty(n)
y = np.empty(n)
a = np.empty(n)
v[0] = 10

#a = Dvy|vy| -g

floor = np.zeros(t.size)

for i in range(n-1):    
    a[i] = -D * v[i]*abs(v[i]) - g
    v[i+1] = v[i] + a[i]*dt
    y[i+1] = y[i] + v[i] * dt

a[n-1] = -D * v[n-1]*abs(v[n-1]) - g


tmax = 10/9.8
    
for i in range(n-1):
    if (v[i]>(0-dt) and v[i+1] <(0+dt)):
        #print("dt, t, y = ", dt, t[i+1], y[i+1])
        print("A posição max é {:0.2f} m".format(y[i+1]))
        plt.plot(t[i+1],y[i+1], "o", label="y(t) max")
        break

for i in range(n-1):
    if (y[i]>(0-dt) and y[i+1] <(0+dt)):
        #print("dt, t, y = ", dt, t[i+1], y[i+1])
        print("Volta a passar pela posição inical no instante {:0.2f} s".format(t[i+1]))
        plt.plot(t[i+1],y[i+1], "o", label="t(0)")
        break

    
plt.xlabel('tempo (s)')
plt.ylabel('X (m)')
plt.plot(t, y, label="Posição com resistência do ar, vt = 100km/h")
plt.legend()
plt.show()
plt.xlabel('tempo (s)')
plt.ylabel('v (m/s)')
plt.plot(t, v, label="Velocidade com resistência do ar, vt = 100km/h")
plt.legend()
plt.show()
plt.xlabel('tempo (s)')
plt.ylabel('a (m/s^2)')
plt.plot(t, a, label="Acelaração com resistência do ar, vt = 100km/h")

plt.legend()
plt.show()