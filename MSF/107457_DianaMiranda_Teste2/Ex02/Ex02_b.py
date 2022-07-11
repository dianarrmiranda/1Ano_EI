import matplotlib.pyplot as plt
import numpy as np

#c) Quanto tempo leva a percorrer 2 km?
#Calcular Potência

u = 0.01
m = 60+12
Area = 0.5
par = 1.225
g=9.8
Cres = 0.9

P = 0.48 * 735.499

t0 = 0
tf =2000
dt = 0.001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

vx = np.empty(n)
v = np.empty(n)
ax = np.empty(n)
x = np.empty(n)

vx[0] = 0.5
ax[0] = 0
x[0] = 0


for i in range(n-1):   
    
    v[i] = np.sqrt(vx[i]**2)
    ax[i+1] = -u*g - (Cres*Area*par*v[i]*vx[i])/(2*m) + P/(m*v[i])
    vx[i+1] = vx[i] +ax[i]*dt
    x[i+1] = x[i] + vx[i] * dt
    
v[n-1] = np.sqrt(vx[n-1]**2)


#Calcular tempo leva a percorrer 2 km?
for i in range(n-1):
    if (x[i]>2000-dt and x[i]>2000+ dt): #é 2000m - 2km
        print("tempo = {:0.2f} s".format( t[i]))
        plt.plot(t[i],v[i], "o", label="posição 2")
        break
    
plt.plot(t,v)
plt.xlabel("t (s)")
plt.ylabel("v (m/s)")
plt.title("Velocidade Terminal")
plt.show()