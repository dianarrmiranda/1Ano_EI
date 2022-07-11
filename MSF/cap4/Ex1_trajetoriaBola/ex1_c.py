
import matplotlib.pyplot as plt
import numpy as np

#c) Nas condições da alínea a), qual o alcance (distância entre a posição onde foi
#chutada e o ponto onde alcançou no campo) da trajetória da bola e quanto tempo
#demorou?

v0 = 27.7778 # m/s
teta = np.radians(10)
dt = 0.001
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
    
for i in range(n-1):
    if (y[i+1]*y[i]<0):
        print("Demorou {:0.2f}s".format(t[i]))
        print("Alcance {:0.2f}m".format(x[i]))
        plt.plot(t[i],y[i], "o", label="y(t) = 0")
        break
    
plt.plot(t,y)
plt.xlabel("t (s)")
plt.ylabel("y(t) (m)")
plt.title("Trajetória da bola - Só considerando peso da bola")
plt.show()
