#e) Calcule a energia mecânica. É constante ao longo do tempo?

import matplotlib.pyplot as plt
import numpy as np

m = 1
k = 1
g=9.8

xeq = 0
b=0.05 #Kg/s
f=7.5
wf=1

alpha = 0.002 #N/m^2
t0 = 0
tf =200
dt = 0.0001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)
Ep = np.empty(n)
Ec = np.empty(n)
EM = np.empty(n)


x[0] = 0
v[0] = 0



for i in range(n-1):   
    a[i] = (-k/m)*x[i]*(1+2*alpha*x[i]**2)-(b*v[i])/m + f*np.cos(wf * t[i])/m
    v[i+1] = v[i] +a[i]*dt 
    x[i+1] = x[i] +v[i]*dt
    Ep[i] = 0.5*k* x[i]**2
    Ec[i] = m*0.5*v[i]**2
    EM[i] = Ec[i] + Ep[i]
    
Ep[n-1] = 0.5*k*x[n-1]**2
Ec [n-1]= m*0.5*v[n-1]**2
EM[n-1] = Ec[n-1] + Ep[n-1]


plt.plot(t,EM)
plt.xlabel("t (s)")
plt.ylabel("EM (j)")
plt.title("")
plt.show()

#Não é. O sistema recebe energia
#realizada pela força externa e dissipa energia devido à resistência do meio.
