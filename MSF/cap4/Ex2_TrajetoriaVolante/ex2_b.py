import matplotlib.pyplot as plt
import numpy as np

#Em ponto cai no chão e quanto demorou?

v0 = 200/3.6 # m/s
x0 = 0
y0 =3
teta = np.radians(10)
dt = 0.0001
g = 9.8
t0 = 0
tf =1.5
vt = 6.80 #m/s

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

vx = np.empty(n)
vy = np.empty(n)
ay = np.empty(n)
ax = np.empty(n)

y = np.empty(n)
x = np.empty(n) 

#valor inciais em cada eixo
ay0 = -g
ax0 = 0
    
x[0] = x0
y[0] = y0
vx[0] = v0*np.cos(teta)
vy[0] = v0*np.sin(teta)

D = g/vt**2

for i in range(n-1):    

    ax[i] = ax0-D*np.sqrt(vx[i]**2+vy[i]**2)*vx[i]
    ay[i] = ay0-D*np.sqrt(vx[i]**2+vy[i]**2)*vy[i]
    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] +ax[i]*dt
    y[i+1] = y[i] + vy[i] * dt
    x[i+1] = x[i] + vx[i] * dt

#Quanto tempo demorou a trajetória? 
for i in range(n-1):
    if (y[i+1]*y[i]<0):
        print("Demorou {:0.2f}s".format(t[i]))
        print("Alcance {:0.2f}m".format(x[i]))
        plt.plot(x[i],y[i], "o", label="y(t) = 0")
        break

plt.plot(x,y)
plt.xlabel("x (m)")
plt.ylabel("y(t) (m)")
plt.title("Trajetória da volante")
plt.show()



