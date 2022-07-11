import matplotlib.pyplot as plt
import numpy as np

v0 = 27.7778 # m/s
teta = np.radians(10)
dt = 0.0001
g = 9.8
t0 = 0
tf =1

vt= 27.7778 # m/s

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

vx = np.empty(n)
vy = np.empty(n)
ay = np.empty(n)
ax = np.empty(n)
y = np.empty(n)
x = np.empty(n) 
v = np.empty(n)

x[0] = v0*np.cos(teta)*t[0] 
y[0] = v0*np.sin(teta)*t[0] - g*t[0]**2
vx[0] = v0*np.cos(teta)
vy[0] = v0*np.sin(teta)

d = g/vt**2


for i in range(n-1):    
    v[i] = np.sqrt(vx[i]**2 + vy[i]**2)
    ay[i] = -d*abs(v[i])*vy[i]-g
    ax[i] = -d*vx[i]*abs(v[i])
    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] +ax[i]*dt
    y[i+1] = y[i] + vy[i] * dt
    x[i+1] = x[i] + vx[i] * dt


plt.plot(x,y, label = "Euler com resistência do ar")
#Máximo 
for i in range(n-1):
    if (y[i+1]<y[i]):
        print("A altura max é {:0.2f}m aos {:0.2f}s".format(y[i],t[i]))
        plt.plot(x[i],y[i], "o", label="y(t) max")
        break

plt.show()