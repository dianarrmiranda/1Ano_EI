import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

v0 = 100/3.6 # m/s
teta = np.radians(16)
dt = 0.0001
g = 9.8
t0 = 0
tf =3
vt= 100/3.6 # m/s

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

vx = np.empty(n)
vy = np.empty(n)
vz = np.empty(n)

ax = np.empty(n)
ay = np.empty(n)
az = np.empty(n)

x = np.empty(n) 
y = np.empty(n)
z = np.empty(n)

#valor inciais em cada eixo
ay0 = -g
ax0 = 0
    

x[0] = 0
y[0] = 0
z[0] = 0

vx[0] = v0*np.cos(teta)
vy[0] = v0*np.sin(teta)
vz[0] = 0

v = np.empty(n)

d = g/vt**2

for i in range(n-1):    

    ax[i] = -d*vx[i]*abs(v[i])
    ay[i] = -d*abs(v[i])*vy[i]-g
    az[i] = 0
    
    vx[i+1] = vx[i] +ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt
    vz[i+1] = vz[i] +az[i]*dt
    
    x[i+1] = x[i] + vx[i] * dt
    y[i+1] = y[i] + vy[i] * dt
    z[i+1] = z[i] + vz[i] * dt

for i in range(n-1):
    if (x[i]>20+dt and x[i]>20-dt):
        print("Passa a baliza {:0.2f} m".format(y[i]))
        plt.plot(x[i],y[i], "o", label="x>20")
        break
    
for i in range(n-1):
    if x[i] > 20 and (-3.75 < z[i] <3.75) and (0<y[i]<2.4):
        print('Entrou')
        break

plt.plot(x,y)
plt.xlabel("x (m)")
plt.ylabel("y(t) (m)")
plt.title("Método de Euler, dt=0.0001")
plt.show()



