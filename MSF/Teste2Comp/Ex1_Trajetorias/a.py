
import matplotlib.pyplot as plt
import numpy as np

v0 = 140/3.6 # m/s
teta = np.radians(7)
dt = 0.0001
g = 9.8
t0 = 0
tf =1
vt = 100/3.6 #m/s

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

vx = np.empty(n)
vy = np.empty(n)
ay = np.empty(n)
ax = np.empty(n)

y = np.empty(n)
x = np.empty(n) 

v = np.empty(n)
aresx = np.empty(n)
aresy = np.empty(n)

x[0] = v0*np.cos(teta)*t[0] 
y[0] = v0*np.sin(teta)*t[0] - g*t[0]**2
vx[0] = v0*np.cos(teta)
vy[0] = v0*np.sin(teta)

#Cálculo resistência do ar
D = g/vt**2

for i in range(n-1):    
    v[i] = np.sqrt(vx[i]**2 + vy[i]**2)

    aresx[i] = -D*vx[i]*abs(v[i])
    ax[i] = aresx[i]
    aresy[i] = -D*abs(v[i])*vy[i]
    ay[i] =  aresy[i] - g 
    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] +ax[i]*dt
    y[i+1] = y[i] + vy[i] * dt
    x[i+1] = x[i] + vx[i] * dt
    
for i in range(n-1):
    if (y[i+1]*y[i]<0):
        print("Demorou {:0.2f}s".format(t[i]))
        print("Alcance {:0.2f}m".format(x[i]))
        plt.plot(x[i],y[i], "o", label="y(t) = 0")
        break
    

plt.plot(x,y)
plt.xlabel("x (m)")
plt.ylabel("y(t) (m)")
plt.title("Trajetória da bola")
plt.show()
