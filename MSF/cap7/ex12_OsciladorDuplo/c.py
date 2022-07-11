import matplotlib.pyplot as plt
import numpy as np

#b) Calcule a lei do movimento, quando a energia total for 3 J. Qual a amplitude e a frequência do movimento?

m = 1
k = 1
g=9.8

xeq = 1.5

t0 = 0
tf =20
dt = 0.0001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)
Ep = np.empty(n)
Ec = np.empty(n)
EM = np.empty(n)
#x[0] = sqrt(sqrt(em/k)+xeq**2)

em = 3 #j

x[0] = np.sqrt(np.sqrt(2*em/k)+xeq**2)
v[0] = 0

a[0] = -k/m*x[0]

for i in range(n-1):   
    a[i+1] = -2*k/m*(x[i]**2-xeq**2)*x[i]
    v[i+1] = v[i] +a[i+1]*dt #a[i+1] - euler cromer
    x[i+1] = x[i] +v[i+1]*dt
    Ep[i] = 0.5*k*(x[i]**2-xeq**2)**2
    Ec[i] = m*0.5*v[i]**2
    EM[i] = Ec[i] + Ep[i]
    
Ep[n-1] = 0.5*k*(x[n-1]**2-xeq**2)**2
Ec [n-1]= m*0.5*v[n-1]**2
EM[n-1] = Ec[n-1] + Ep[n-1]

arrayMaximos = []
arrayMinimos= []
temposMax = []
temposMin = []

for i in range(n-1):
    if (x[i-1]<x[i]>x[i+1] and i>0 ): 
        arrayMaximos.append(x[i])
        temposMax.append(t[i])
    if (x[i-1]>x[i]<x[i+1] and i>0 ): 
        arrayMinimos.append(x[i])
        temposMin.append(t[i])
        
periodos = []

for i in range(len(temposMax)-1):
    periodos.append(temposMax[i+1] - temposMax[i])


amplitude = sum(arrayMaximos)/len(arrayMaximos)
minimo = sum(arrayMinimos)/len(arrayMinimos)

periodoMedia = sum(periodos)/len(periodos)

print("A amplitude média é {:.2f} m (Limite Máximo)".format(amplitude))
print("Limite Minimo é {:.2f} m".format(minimo))
print("A frequência é {:.3f} Hz".format(1/periodoMedia))

plt.plot(t,x)
plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.title("Lei do movimento, quando a energia total for 0.75J")
plt.show()

plt.plot(x,Ep)
plt.xlabel("x (m)")
plt.ylabel("EP (J)")
plt.title("Energia Potencial, quando a energia total for 1J")
plt.show()

