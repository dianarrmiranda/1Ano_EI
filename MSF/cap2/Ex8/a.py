#Calcule o instante em que cada objeto chega ao solo. A velocidade terminal é de 6,80
#m/s e 100 km/h para o volante de badmington e a bola de ténis, respetivamente.

import matplotlib.pyplot as plt
import numpy as np

m = 58 #g

y0 = 5 #m
v0 = 0

vtVB = 6.8 #m/s
vtBT = 100*(1000/3600) #m/s 100km/h
g = 9.8
dt = 0.001

t0 = 0
tf = 1.5+dt

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)
v = np.empty(n)
y = np.empty(n)
a = np.empty(n)
v[0] = v0
y[0] = y0

DVB = g/vtVB**2
DBT = g/vtBT**2 

for i in range(n-1):    
    a[i] = -DVB * v[i]*abs(v[i]) - g
    v[i+1] = v[i] + a[i]*dt
    y[i+1] = y[i] + v[i] * dt

a[n-1] = - DVB * v[n-1]*abs(v[n-1]) - g

for i in range(n-1):
    if (y[i]>(0-dt) and y[i+1] <(0+dt)):
        #print("dt, t, y = ", dt, t[i+1], y[i+1])
        print("Volante de Badminton chega ao solo em {:0.2f} s".format(t[i+1]))
        plt.plot(t[i+1],y[i+1], "x", label="Solo Volante de Badminton")
        break

plt.plot(t, y, label="Posição Volante Badminton")

for i in range(n-1):    
    a[i] = -DBT * v[i]*abs(v[i]) - g
    v[i+1] = v[i] + a[i]*dt
    y[i+1] = y[i] + v[i] * dt

a[n-1] = - DBT * v[n-1]*abs(v[n-1]) - g
for i in range(n-1):
    if (y[i]>(0-dt) and y[i+1] <(0+dt)):
        #print("dt, t, y = ", dt, t[i+1], y[i+1])
        print("Bola de Tênis chega ao solo em {:0.2f} s".format(t[i+1]))
        plt.plot(t[i+1],y[i+1], "x", label="Solo Bola de Tênis")
        break

plt.plot(t, y, label="Posição Bola de Tênis")


plt.xlabel('tempo (s)')
plt.ylabel('y (m)')
plt.legend()
plt.show()





