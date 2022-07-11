import matplotlib.pyplot as plt
import numpy as np

#Considere agora a resistência do ar. 

v0 = 27.7778 # m/s
teta = np.radians(10)
dt = 0.01
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

#Conifas no resultado?
x0 = x[0]
y0 = y[0]
vx0 = vx[0]
vy0 = vy[0]
xanalitico =  vx0*t +x0
yanalitico = vy0*t- (1/2)*g*t**2 + y0

plt.plot(xanalitico,yanalitico, label = "Analitico sem resistência do ar")

plt.legend()
plt.show()