import matplotlib.pyplot as plt
import numpy as np

#b)  Faça o gráfico da lei do movimento. Qual é o seu período?

m = 1
k = 1

xeq =2

x0 = 3 
v0 = 0


t0 = 0
tf =30
dt = 0.001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)

em=np.zeros(n)


x[0] = x0
v[0] = v0

em[0]= 0.5*(np.abs(x[0])-xeq)**2*m + 0.5* v[0]**2*m

a[0] = -x[0] + xeq

for i in range(n-1):  
    
    v[i+1]=v[i]+a[i]*dt
    x[i+1] =x[i]+v[i+1]*dt

    if x[0]<0:
        a[i+1]= -x[i+1] - xeq
    else:
        a[i+1]= -x[i+1] + xeq
    
    em[i]=  0.5*(np.abs(x[i])- xeq)**2*m + 0.5*v[i]**2*m

em[n-1]=  0.5*(np.abs(x[n-1])- xeq)**2*m + 0.5*v[n-1]**2*m

print("-----------------Alinea (b)-------------------")
arrayMaximos = []
temposMax = []

for i in range(n-1):
    if (x[i-1]<x[i]>x[i+1] and i>0 ): 
        arrayMaximos.append(x[i])
        temposMax.append(t[i])
        
periodos = []

for i in range(len(temposMax)-1):
    periodos.append(temposMax[i+1] - temposMax[i])


amplitude = sum(arrayMaximos)/len(arrayMaximos)

periodoMedia = sum(periodos)/len(periodos)

print("A amplitude média é {:.4f} m".format(amplitude))
print("O periodo médio é {:.3f} s".format(periodoMedia))

plt.plot(t,x)
plt.xlabel('t(s)') 
plt.ylabel('x(m)')
plt.grid(True)
plt.show()

