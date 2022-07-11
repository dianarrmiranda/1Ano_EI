from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

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
        print("Alcance {:0.2f}m".format(x[i]))
        break
    
for i in range(n-1):
    if (y[i+1]<y[i]):
        print("A altura max é {:0.2f}m aos {:0.2f}s".format(y[i],t[i]))
        break


plt.title("Lei do movimento em x")
plt.plot(t,x)
plt.show()
plt.title("Lei do movimento em y")
plt.plot(t,y)
plt.show()
plt.title("Lei da velocidade em x")
plt.plot(t,vx)
plt.show()
plt.title("Lei da velocidade em y")
plt.plot(t,vy)
plt.show()
