import matplotlib.pyplot as plt
import numpy as np

u = 0.01
m = 60+12
Area = 0.5
par = 1.225
g=9.8
Cres = 0.9

P = 0.48 * 735.499

t0 = 0
tf =150
dt = 0.001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

vx = np.empty(n)
v = np.empty(n)
ax = np.empty(n)

vx[0] = 0.5
ax[0] = 0

for i in range(n-1):   
    v[i] = np.sqrt(vx[i]**2)
    ax[i+1] = -u*g - (Cres*Area*par*v[i]*vx[i])/(2*m) + P/(m*v[i])
    vx[i+1] = vx[i] +ax[i]*dt
    
v[n-1] = np.sqrt(vx[n-1]**2)


#Calcular velocidade terminal
for i in range(n-1):
    if (t[i]>100-dt and t[i]>100+dt ):
        print("Velocidade terminal = {:0.2f} m/s".format(vx[i]))
        plt.plot(t[i],vx[i], "o", label="vt")
        break
      
    
plt.plot(t,vx)
plt.xlabel("t (s)")
plt.ylabel("v (m/s)")
plt.title("Velocidade Terminal")
plt.show()
