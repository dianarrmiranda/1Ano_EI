import matplotlib.pyplot as plt
import numpy as np

#a) A rotação é nula.

v0 = 130/3.6 # m/s
teta = np.radians(10)
dt = 0.0001
g = 9.8
t0 = 0
tf =1.4

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

x[0] = -10
y[0] = 1
z[0] = 0

vx[0] = v0*np.cos(teta)
vy[0] = v0*np.sin(teta)
vz[0] = 0

v = np.empty(n)

d = g/vt**2

for i in range(n-1):    
    v[i] = np.sqrt(vx[i]**2 + vy[i]**2)
    
    ay[i] = -d*abs(v[i])*vy[i]-g
    ax[i] = -d*vx[i]*abs(v[i])
    az[i] = 0
    
    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] +ax[i]*dt
    vz[i+1] = vz[i] +az[i]*dt
    
    y[i+1] = y[i] + vy[i] * dt
    x[i+1] = x[i] + vx[i] * dt
    z[i+1] = z[i] + vz[i] * dt
    
    
for i in range(n-1):
    if (y[i+1]<y[i]):
        print("A altura max é {:0.2f} m".format(y[i]))
        plt.plot(x[i],y[i], "o", label="Altura máxima")
        break
    
for i in range(n-1):
    if (y[i+1]*y[i]<0):
        print("Alcance {:0.2f} m".format(x[i]))
        plt.plot(x[i],y[i], "o", label="Alcance")
        break
    
plt.plot(x,y)
plt.legend()
plt.show()