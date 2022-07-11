import matplotlib.pyplot as plt
import numpy as np

#b) A frequência angular da oscilação considerando agora que o amortecimento afeta a
#oscilação.

m=1 
k=1
wf=1.0
fo=7.5
b=0.16
tf=50
ti=0    
dt= 0.0001
n=int((tf-ti)/dt)
t=np.linspace(ti,n*dt,n)


x0=2
v0=3
a0=0

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)

x[0]=x0
v[0]=v0

for i in range (n-1):
    a[i+1] = -k/m*(x[i])-(b*(v[i]))/m
    v[i+1] = v[i] +a[i+1]*dt #a[i+1] - euler cromer
    x[i+1] = x[i] +v[i+1]*dt
    
arrayMaximos = []
temposMax = []

for i in range(n-1):
    if (x[i-1]<x[i]>x[i+1] and i>0 ): 
        arrayMaximos.append(x[i])
        temposMax.append(t[i])

amplitude = sum(arrayMaximos)/len(arrayMaximos)


print("A amplitude média é {:.2f} m (Limite Máximo)".format(amplitude))


print("-----------------Alinea (c)-------------------")
for i in range(len(arrayMaximos)):
    plt.plot(t[i],arrayMaximos[i], "o")
    
plt.xlabel('t(s)') 
plt.ylabel('x(m)')
plt.grid(True)
plt.show()
