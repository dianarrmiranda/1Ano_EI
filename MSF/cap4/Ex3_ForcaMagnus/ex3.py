import matplotlib.pyplot as plt
import numpy as np

dt = 0.001
massa = 0.45 #kg - 450g
r = 0.11 #m - 11cm
area = np.pi*r**2
PAr = 1.225 #kg/m^3
vt = 100/3.6 #m/s

tf = 0.5
t0 = 0

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

g = 9.8

x = np.empty(n)
vx = np.empty(n)
Wx = 0

ax = np.empty(n)
ay = np.empty(n)
az = np.empty(n)

y = np.empty(n)
vy = np.empty(n)
Wy = 400 #omega 

z = np.empty(n)
vz = np.empty(n)

Wz = 0

x[0]=0
y[0]=0
z[0] = 23.8

vx[0] = 25.5
vy[0] = 5
vz[0] = -50



for i in range(n-1):
    vv=np.sqrt(vx[i]**2+vy[i]**2+vz[i]**2)
    dres=g/vt**2
    mag=0.5*1.225*0.11*np.pi*0.11**2
    
    amx=mag*Wy*vz[i]/massa
    amz=-mag*Wy*vx[i]/massa
    
    ax[i]=-dres*vv*vx[i]+amx
    ay[i]=-g-dres*vv*vy[i]
    az[i]=-dres*vv*vz[i]+amz
    
    vx[i+1]=vx[i]+ax[i]*dt
    vy[i+1]=vy[i]+ay[i]*dt
    vz[i+1]=vz[i]+az[i]*dt
    
    x[i+1]=x[i]+vx[i]*dt
    y[i+1]=y[i]+vy[i]*dt
    z[i+1]=z[i]+vz[i]*dt

for i in range(n-1):
    if x[i] < 0 and (z[i]>0 and z[i]<7.3) and (y[i]>0 and y[i]<2.4):
        print('Entrou')
        break
    
plt.plot(t,x,label="x")
plt.plot(t,y,label="y")
plt.plot(t,z,label="z")
plt.title("Bola com rotação (x,y,z) em função do tempo")
plt.xlabel("x,y,z (m)")
plt.ylabel("t (s)")
plt.legend()
plt.show()