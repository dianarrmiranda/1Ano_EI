import matplotlib.pyplot as plt
import numpy as np

m = 0.5
k = 2
g=9.8

xeq = 0

alpha = -0.1
beta = 0.02

t0 = 0
tf =200
dt = 0.001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)
Ep = np.empty(n)
Ec = np.empty(n)
EM = np.empty(n)
zeros = np.empty(n)
em = 4

x[0] = 0
v[0] = np.sqrt(2*em/m)

a[0] = -k/m*x[0] - (3*alpha*(x[0]**2))/m + (4*beta*(x[0]**3))/m

for i in range(n-1):   
    a[i+1] = -k/m*x[i] - (3*alpha*(x[i]**2))/m + (4*beta*(x[i]**3))/m
    v[i+1] = v[i] +a[i+1]*dt #a[i+1] - euler cromer
    x[i+1] = x[i] +v[i+1]*dt
    
    Ep[i] =  0.5*k*(x[i]**2) + alpha*(x[i]**3) - beta*(x[i]**4)
    EM[i] = 0.5*m*v[i]**2 + Ep[i]
    
    zeros[i] = 4
    
Ep[n-1] = 0.5*k*(x[n-1]**2) + alpha*(x[n-1]**3) - beta*(x[n-1]**4)
EM[n-1] = 0.5*m*v[n-1]**2 + Ep[n-1]

zeros[n-1] = 4


plt.plot(x,Ep)
plt.plot(x,zeros)
plt.xlabel("x (m)")
plt.ylabel("EP (J)")
plt.title("Energia Potencial, quando a energia menor for 4J")
plt.show()

