import matplotlib.pyplot as plt
import numpy as np

#b) Calcule a lei do movimento, quando a posição inicial for 3.5 m e a velocidade inicial 2.0 m/s? Quanto é a
#energia mecânica? Entre que limites se efetua o movimento e a frequência e o período do movimento?

m = 0.5
k = 1.8
g=9.8

xeq = 0

beta = 0.9

x0=2.5
v0=3

t0 = 0
tf = 5
dt = 0.0001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)
Ep = np.empty(n)
Ec = np.empty(n)
EM = np.empty(n)

x[0] = x0
v[0] = v0

a[0] = -k/m*x[0] - (4*beta*(x[0]**3))/m

for i in range(n-1):  
    a[i+1] =-k/m*x[i] - (4*beta*(x[i]**3))/m
    v[i+1] = v[i] +a[i+1]*dt #a[i+1] - euler cromer
    x[i+1] = x[i] +v[i+1]*dt
    
    Ep[i] = 0.5*k*(x[i]**2) + beta*(x[i]**4)
    EM[i] = 0.5*m*v[i]**2 + Ep[i]
    
Ep[n-1] = 0.5*k*(x[n-1]**2) + beta*(x[n-1]**4)
EM[n-1] = 0.5*m*v[n-1]**2 + Ep[n-1]

print("-----------------Alinea (b)-------------------")
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

print("A amplitude média é {:.4f} m (Limite Máximo)".format(amplitude))
print("Limite Minimo é {:.4f} m".format(minimo))
print("A frequência é {:.4f} Hz".format(1/periodoMedia))
print("O período é {:.4f} s".format(periodoMedia))
print("Energia Mecânica {:.4f} J".format(EM[n-1]))


plt.plot(t,x)
plt.xlabel('t(s)') 
plt.ylabel('x(m)')
plt.grid(True)
plt.show()

plt.plot(t,EM)
plt.xlabel('t(s)') 
plt.ylabel('EM(J)')
plt.grid(True)
plt.show()
