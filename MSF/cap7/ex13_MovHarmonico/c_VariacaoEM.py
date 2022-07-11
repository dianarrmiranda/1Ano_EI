import matplotlib.pyplot as plt
import numpy as np

#a)Determine a energia cinética e energia potencial elástica do oscilador no instante de
#tempo em que elas são iguais

m = 1
k = 100
g=9.8

A = 0.1 #m
bc = 2 #kg/s

b = bc * 1.08 

t0 = 0
tf = 30
dt = 0.0001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)
Ep = np.empty(n)
Ec = np.empty(n)
EM = np.empty(n)

x[0] = 0.1*np.cos(10*t[0])
v[0] = 0

a[0] = -k/m*(x[0])-(b*(v[0]))/m


for i in range(n-1):   
    a[i+1] = -k/m*(x[i])-(b*(v[i]))/m
    v[i+1] = v[i] +a[i+1]*dt #a[i+1] - euler cromer
    x[i+1] = x[i] +v[i+1]*dt
    Ep[i] = 0.5*k*(x[i]**2)
    Ec[i] = m*0.5*(v[i]**2)
    EM[i] = Ec[i] + Ep[i]

for i in range(n-1):
    if (t[i]>(1.0785-dt) and t[i+1] <(1.0785+dt)):
        #print("dt, t, y = ", dt, t[i+1], y[i+1])
        print("EM {:0.4f} J".format(EM[i]))
        break

    
Ep[n-1] = 0.5*k*x[n-1]**2
Ec [n-1]= m*0.5*v[n-1]**2
EM[n-1] = Ec[n-1] + Ep[n-1]

plt.plot(t, EM)
plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.show()

