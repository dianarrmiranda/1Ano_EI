import matplotlib.pyplot as plt
import numpy as np

#a)Determine a energia cinética e energia potencial elástica do oscilador no instante de
#tempo em que elas são iguais

m = 1
k = 100
g=9.8

A = 0.1
t0 = 0
tf = 40
dt = 0.0001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)
Ep = np.empty(n)
Ec = np.empty(n)
EM = np.empty(n)

x[0] = 10*np.cos(10*t[0])
v[0] = 0

a[0] = -1000*np.cos(A*t[0])


for i in range(n-1):   
    a[i+1] = -A*(10**2)*np.cos(10*t[i+1])
    v[i+1] = -A*10*np.sin(10*t[i+1])
    x[i+1] = A* np.cos(10*t[i+1])
    Ep[i] = 0.5*k*(x[i]**2)
    Ec[i] = m*0.5*(v[i]**2)
    EM[i] = Ec[i] + Ep[i]
    
    if(Ep[i] > 0.25):
        print("Energia cinética e potencial elástica são iguais : ", t[i] )
        break
    
    
Ep[n-1] = 0.5*k*x[n-1]**2
Ec [n-1]= m*0.5*v[n-1]**2
EM[n-1] = Ec[n-1] + Ep[n-1]

plt.plot(x,Ep)
plt.xlabel("x (m)")
plt.ylabel("EP (J)")
plt.title("Energia Potencial, quando a energia total for 1J")
plt.show()

plt.plot(x,EM)
plt.xlabel("x (m)")
plt.ylabel("EM (J)")
plt.title("Energia Mecânica, quando a energia total for 1J")
plt.show()
