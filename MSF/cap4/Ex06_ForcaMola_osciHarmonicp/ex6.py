
import matplotlib.pyplot as plt
import numpy as np

dt = 0.0001
m = 1
k = 1
w = np.sqrt(k/m)
tf = 18 ##tempo final
t0=0
n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)
A = 4
O = 0

fi=0

x0 = 4
v0x = 0

vx = np.empty(n)
x = np.empty(n)
x[0] = x0
vx[0] = v0x

vxExato = -A*w*np.sin(w*t+ fi)

xExato = A*np.cos(w*t+ fi)

#metodo de Euler-Cromer
for i in range(n-1):
    ax = -k/m * x[i]
    vx[i+1] = vx[i] + ax * dt
    x[i+1] = x[i] + vx[i+1] *dt
    
#b
plt.xlim([0,17.5])
plt.plot(t,vx,"o" ,label= "Euler Cromer")
plt.plot(t,vxExato,label= "Exato")
plt.title("Lei da velocidade")
plt.legend()
plt.show()

#c
plt.xlim([0,17.5])
plt.plot(t,x,"o" ,label= "Euler Cromer")
plt.plot(t,xExato,label= "Exato")
plt.title("Lei do movimento")
plt.legend()
plt.show()

#𝑣𝑥(t) = − 𝐴 𝜔 sin( 𝜔 𝑡 + 𝜙); 