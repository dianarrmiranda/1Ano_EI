import matplotlib.pyplot as plt
import numpy as np

#a) Calcule a lei do movimento, quando a posição inicial for 1.3 m e a velocidade inicial
#nula.

m=1 
k=1

b=0.16

tf=50
ti=0    
dt= 0.0001
n=int((tf-ti)/dt)
t=np.linspace(ti,n*dt,n)


x0=1.3
v0=0
a0=0

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)

x[0]=x0
v[0]=v0

for i in range (n-1):
    a[i+1] = -k/m*(x[i])-(b*(v[i]))/m
    v[i+1] = v[i] +a[i+1]*dt #a[i+1] - euler cromer
    x[i+1] = x[i] +v[i+1]*dt

print("-----------------Alinea (c)-------------------")

plt.plot(t,x)
plt.xlabel('t(s)') 
plt.ylabel('x(m)')
plt.grid(True)
plt.show()


