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

v = np.empty(n)

x[0] = 0
y[0] = 0
z[0] = 0

vx[0] = v0*np.cos(teta)
vy[0] = v0*np.sin(teta)
vz[0] = 0

#Força Magnus -------------------
wz = -10
par = 1.225
r= 0.11 #m
A = np.pi*r**2
massa= 0.45 #kg
c = 1/2 * A * par * r 
#--------------------------------

d = g/vt**2

for i in range(n-1):    
    v[i] = np.sqrt(vx[i]**2 + vy[i]**2)
    
    amx = c*wz*vy[i] #Força magnus
    amy = -c*wz*vx[i] #Força magnus
    
    ax[i] = -d*vx[i]*abs(v[i]) + amx / massa #Acelaração com Força magnus
    ay[i] = -d*abs(v[i])*vy[i]-g + amy / massa #Acelaração com Força magnus
    az[i] = -d*abs(v[i])*vz[i] 
    
    vx[i+1] = vx[i] +ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt
    vz[i+1] = vz[i] +az[i]*dt
    
    y[i+1] = y[i] + vy[i] * dt
    x[i+1] = x[i] + vx[i] * dt
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
plt.legend()
plt.show()