import matplotlib.pyplot as plt
import numpy as np


#a) Calcule numericamente a lei do movimento, no caso em que a velocidade inicial é nula e a posição inicial 4 m.

m = 1
k = 1
g=9.8


t0 = 0
tf =30
dt = 0.01

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)

x[0] = 2
v[0] = -3

a[0] = -k/m*x[0]

for i in range(n-1):   
    a[i+1] = -k/m*x[i]
    v[i+1] = v[i] +a[i+1]*dt #a[i+1] - euler cromer
    x[i+1] = x[i] +v[i+1]*dt
    

plt.plot(t,x)
plt.xlabel("t (s)")
plt.ylabel("x (m/s)")
plt.title("Lei do movimento")
plt.show()
