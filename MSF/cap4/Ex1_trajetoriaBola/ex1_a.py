import matplotlib.pyplot as plt
import numpy as np

#a) Encontre a lei do movimento usando métodos analíticos, se só considerar o peso da
#bola. Faça um gráfico da altura em função da distância percorrida na horizontal.


v0 = 27.7778 # m/s 100km/3.6
teta = np.radians(10)
dt = 0.0001
g = 9.8
t0 = 0
tf =1

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

vx = np.empty(n)
vy = np.empty(n)
ay = np.empty(n)
ax = np.empty(n)

y = np.empty(n)
x = np.empty(n) 

x[0] = v0*np.cos(teta)*t[0] 
y[0] = v0*np.sin(teta)*t[0] - g*t[0]**2
vx[0] = v0*np.cos(teta)
vy[0] = v0*np.sin(teta)

for i in range(n-1):    
    ay[i] = -g
    ax[i] = 0
    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] +ax[i]*dt
    y[i+1] = y[i] + vy[i] * dt
    x[i+1] = x[i] + vx[i] * dt

plt.plot(x,y)
plt.xlabel("x (m)")
plt.ylabel("y(t) (m)")
plt.title("Trajetória da bola - Só considerando peso da bola")
plt.show()
