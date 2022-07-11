import matplotlib.pyplot as plt
import numpy as np


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

#---------------------------------------

m = 0.5
k = 2
g=9.8

xeq = 0

alpha = -0.1
beta = 0.02

v0 = 0.5
x0 = 1.5

t0 = 0
tf =10
dt = 0.001

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

a[0] = -k/m*x[0] - (3*alpha*(x[0]**2))/m + (4*beta*(x[0]**3))/m

for i in range(n-1):   
    a[i+1] = -k/m*x[i] - (3*alpha*(x[i]**2))/m + (4*beta*(x[i]**3))/m
    v[i+1] = v[i] +a[i+1]*dt #a[i+1] - euler cromer
    x[i+1] = x[i] +v[i+1]*dt
    
    Ep[i] =  0.5*k*(x[i]**2) + alpha*(x[i]**3) - beta*(x[i]**4)
    EM[i] = 0.5*m*v[i]**2 + Ep[i]
    
Ep[n-1] = 0.5*k*(x[n-1]**2) + alpha*(x[n-1]**3) - beta*(x[n-1]**4)
EM[n-1] = 0.5*m*v[n-1]**2 + Ep[n-1]

print("-----------------Alinea (c)-------------------")

maxxtotal=0
countmax=0
maxtempos=[]
tempototal=0

ind = np.transpose([0 for i in range(1000)])

#Caluclo da frequência

for i in range(n-1):
    if i>1 and x[i-1] < x[i] and  x[i+1] < x[i]:
        maxt, maxx = maxminv(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])
        maxxtotal += maxx
        countmax+=1
        maxtempos.append(maxt)
        ind[countmax]=int(i) #nota que tem de ser inteiro

t0=ind[countmax-1]
t1=ind[countmax]

for i in range(countmax-1):
    tempototal+=maxtempos[i+1]-maxtempos[i]
    
#Cálculo Periodo
periodos = []

for i in range(len(maxtempos)-1):
    periodos.append(maxtempos[i+1] - maxtempos[i])

periodoMedia = sum(periodos)/len(periodos)
    
print("O período é {:.4f} s".format(periodoMedia))


## Cálculo dos máximos com recurso ao Polinómio de Lagrange. Permite calcular amplitude e mais tarde T
maxGraficos = []
for i in range(n-1):
    if x[i-1] < x[i] and  x[i+1] < x[i]:
        maxt, maxx = maxminv(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])
        if len(maxGraficos) == 0:
            print("O máximo do movimento é {:.4f} m.".format(abs(maxx)))
        maxGraficos.append((maxt,maxx))

for i in range(n-1):
    if x[i-1]>x[i]<x[i+1] and i>0:
        maxt, minx = maxminv(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])
        if minx != maxx:
            print("O minimo do movimento é {:.4f} m.".format(minx))
            break
        else:
            continue

print("A frequência é {:.4f} Hz".format((countmax-1)/tempototal))

plt.plot(t,x)
plt.xlabel('t(s)') 
plt.ylabel('x(m)')
plt.title("Lei do movimento")
plt.grid(True)
plt.show()
