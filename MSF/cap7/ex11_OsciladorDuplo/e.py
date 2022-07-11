import matplotlib.pyplot as plt
import numpy as np

# d) Calcule a lei do movimento quando a energia total for 3 J? Entre que limites se
#efetua o movimento e a frequência do movimento?

def maxminv(xm1,xm2,xm3,ym1,ym2,ym3):  
    # Máximo ou mínimo usando o polinómio de Lagrange
    # Dados (input): (x0,y0), (x1,y1) e (x2,y2) 
    # Resultados (output): xm, ymax 
    xab=xm1-xm2
    xac=xm1-xm3
    xbc=xm2-xm3

    a=ym1/(xab*xac)
    b=-ym2/(xab*xbc)
    c=ym3/(xac*xbc)

    xmla=(b+c)*xm1+(a+c)*xm2+(a+b)*xm3
    xm=0.5*xmla/(a+b+c)

    xta=xm-xm1
    xtb=xm-xm2
    xtc=xm-xm3

    ymax=a*xtb*xtc+b*xta*xtc+c*xta*xtb
    return xm, ymax

m = 1
k = 1

xeq =2
ep = 3.0 #j

x0 = 3 
v0 = 0


t0 = 0
tf =40
dt = 0.0001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

x = np.empty(n)
v = np.empty(n)

em=np.zeros(n)


x[0] = np.abs(xeq+np.sqrt(ep*2/k))
v[0] = v0

em[0]= 0.5*(np.abs(x[0])-xeq)**2*m + 0.5* v[0]**2*m

for i in range(n-1):  
    
    if x[i]>0:
        fx= - x[i]+xeq
    else:
        fx= - x[i]-xeq
    a=fx/m
    
    v[i+1]=v[i]+a*dt
    x[i+1]=x[i]+v[i+1]*dt #euler-cromer
    
    
    em[i]=  0.5*(np.abs(x[i])- xeq)**2+ 0.5*v[i]**2      

em[n-1]=  0.5*(np.abs(x[n-1])- xeq)**2 + 0.5*v[n-1]**2

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

print("A amplitude média é {:.3f} m (Limite Máximo)".format(amplitude))
print("Limite Minimo é {:.3f} m".format(minimo))
print("A frequência é {:.3f} Hz".format(1/periodoMedia))

plt.figure()
plt.plot(t,x)
plt.ylabel('x (m)')
plt.xlabel( 't (s)' )
plt.grid()
plt.show()

