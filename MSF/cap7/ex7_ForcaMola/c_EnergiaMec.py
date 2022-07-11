import matplotlib.pyplot as plt
import numpy as np

#c) Calcule a energia mecânica. É constante ao longo do tempo?

m = 1
k = 1
g=9.8

t0 = 0
tf =30
dt = 0.001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)


x[0] = 4
v[0] = 0

a[0] = -k/m*x[0]

arrayMaximos = []

for i in range(n-1):  
    a[i+1] = -k/m*x[i]
    v[i+1] = v[i] +a[i+1]*dt #a[i+1] - euler cromer
    x[i+1] = x[i] +v[i+1]*dt

EM= m*0.5*v**2 + 0.5*k*x**2

plt.plot(t,EM)
plt.xlabel("t (s)")
plt.ylabel("EM (J)")
plt.ylim(7,9)
plt.title("Energia mecânica")
plt.show()

#A energia mecânica é constante ao longo do tempo.
