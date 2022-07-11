import matplotlib.pyplot as plt
import numpy as np

#b) A rotação é descrita por 𝜔⃗⃗ = (0, 0, +100) rad/s

v0 = 130/3.6 # m/s
teta = np.radians(10)
dt = 0.001
g = 9.8
t0 = 0
tf =2

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

v = np.empty(n)

x[0] = -10
y[0] = 1
z[0] = 0

vx[0] = v0*np.cos(teta)
vy[0] = v0*np.sin(teta)
vz[0] = 0

#Força Magnus -------------------
wz = 100
par = 1.225
r= 0.067/2 #m
A = np.pi*r**2
massa= 0.057
c = 1/2 * A * par * r / massa
#--------------------------------

d = g/vt**2

for i in range(n-1):    
    v[i] = np.sqrt(vx[i]**2 + vy[i]**2)
    
    amx = -c*wz*vy[i] #Força magnus
    amy = c*wz*vx[i] #Força magnus
    
    ax[i] = -d*vx[i]*abs(v[i]) + amx #Acelaração com Força magnus
    ay[i] = -d*abs(v[i])*vy[i]-g + amy #Acelaração com Força magnus
    az[i] = 0
    
    vx[i+1] = vx[i] +ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt
    vz[i+1] = vz[i] +az[i]*dt
    
    x[i+1] = x[i] + vx[i] * dt
    y[i+1] = y[i] + vy[i] * dt
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