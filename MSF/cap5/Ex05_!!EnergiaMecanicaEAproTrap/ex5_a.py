import matplotlib.pyplot as plt
import numpy as np


#a) a) Calcule a energia mecânica em qualquer instante, no caso de não considerar a
#resistência do ar.
#Energia mecânica sem resistencia do ar

v0 = 100/3.6 # m/s
teta = np.radians(10)
dt = 0.01
g = 9.8
t0 = 0
tf =1
m = 0.057

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

for i in range(n-1):    
    ay[i] = -g
    ax[i] = 0
    
    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] +ax[i]*dt
    
    y[i+1] = y[i] + vy[i] * dt
    x[i+1] = x[i] + vx[i] * dt
    
    v[i] = np.sqrt(vx[i]**2 + vy[i]**2)

    Em[i] = 0.5*m*v[i]**2 + m*g*y[i]
 
#Para dar valor ao ultimo indice no array   
v[n-1] = np.sqrt(vx[n-1]**2 + vy[n-1]**2)

Em[n-1] = 0.5*m*v[n-1]**2 + m*g*y[n-1]
#------------------------------------------

for i in range(n-1):
    if (i==0):
        print("Em[{:0.2f}] = {:0.2f}".format(i, Em[i]))  #Energia mecânica no ponto zero t=0
        plt.plot(t[i],Em[i], "o", label="t=0")
    
plt.plot(t,Em)
plt.title("Energia mecânica")
plt.show()