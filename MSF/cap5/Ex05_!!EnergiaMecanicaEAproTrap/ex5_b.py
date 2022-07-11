import matplotlib.pyplot as plt
import numpy as np

#b) Considerando a resistência do ar, calcule a energia mecânica nos três instantes
#𝑡0 = 0, 𝑡1 = 0.4 s e 𝑡2 = 0.8 s.
#Energia mecânica com resistencia do ar

v0 = 100/3.6 # m/s
teta = np.radians(10)
dt = 0.0001
g = 9.8
t0 = 0
tf =1
m = 0.057
vt = 100/3.6

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

vx = np.empty(n)
vy = np.empty(n)

vx[0] = v0*np.cos(teta)
vy[0] = v0*np.sin(teta)

ax = np.empty(n)
ay = np.empty(n)

x = np.empty(n) 
y = np.empty(n)

x[0] = 0
y[0] = 0

#Calcule a energia mecânica
v = np.empty(n)
Em = np.empty(n)
#-----------------

#Cálculo resistência do ar
D = g/vt**2


for i in range(n-1):    
    v[i] = np.sqrt(vx[i]**2 + vy[i]**2)
    
    ax[i] = -D*vx[i]*abs(v[i])
    ay[i] = -D*abs(v[i])*vy[i] - g 
    
    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] +ax[i]*dt
    
    y[i+1] = y[i] + vy[i] * dt
    x[i+1] = x[i] + vx[i] * dt
    
    Em[i] = 0.5*m*v[i]**2 + m*g*y[i]
 
#Para dar valor ao ultimo indice no array  
v[n-1] = np.sqrt(vx[n-1]**2 + vy[n-1]**2)
Em[n-1] = 0.5*m*v[n-1]**2 + m*g*y[n-1]
#------------------------------------------

for i in range(n-1):
    if (i==0):
        print("Em[0] = {:0.2f} J".format(Em[i]))
        plt.plot(t[i],Em[i], "o", label="t=0")
    if (t[i] < 0.4 < t[i+1]):
        print("Em[0.4] = {:0.2f} J".format(Em[i]))
        plt.plot(t[i],Em[i], "o", label="t=0.4")
    if (t[i] < 0.8 < t[i+1]):
        print("Em[0.8] = {:0.2f} J".format(Em[i]))
        plt.plot(t[i],Em[i], "o", label="t=0.8")

    
plt.plot(t,Em)
plt.title("Energia mecânica com resistência do ar")
plt.legend()
plt.show()