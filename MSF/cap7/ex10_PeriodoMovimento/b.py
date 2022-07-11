import matplotlib.pyplot as plt
import numpy as np

def maximo(xm1,xm2,xm3,ym1,ym2,ym3):  # máximo pelo polinómio de Lagrange
    xab=xm1-xm2
    xac=xm1-xm3
    xbc=xm2-xm3
    a=ym1/(xab*xac)
    b=-ym2/(xab*xbc)
    c=ym3/(xac*xbc)
    xmla=(b+c)*xm1+(a+c)*xm2+(a+b)*xm3
    xmax=0.5*xmla/(a+b+c)
    xta=xmax-xm1
    xtb=xmax-xm2
    xtc=xmax-xm3
    ymax=a*xtb*xtc+b*xta*xtc+c*xta*xtb
    return xmax, ymax

l = 1 #Comprimento da Corda
g=9.8

alfa = 5

t0 = 0
tf =15
dt = 0.01

#valores inciais
ang0=np.deg2rad(alfa)
w0=0
aw0=0

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

angulo = np.empty(n)
w = np.empty(n)
aw= np.empty(n)

angulo[0] = ang0
w[0]=w0

maxangtotal=0
countmax=0
maxtempos=[]
tempototal=0

for i in range(n-1):
    aw[i]=-g/l*np.sin(angulo[i])
    w[i+1]=w[i]+aw[i]*dt
    angulo[i+1] =angulo[i]+w[i+1]*dt
        
    if i>1 and angulo[i-1] < angulo[i] and  angulo[i+1] < angulo[i]:
        maxt, maxang=maximo(t[i-1], t[i], t[i+1], angulo[i-1], angulo[i], angulo[i+1])
        maxangtotal +=maxang
        countmax+=1
        maxtempos.append(maxt)
for i in range(countmax-1):
    tempototal+=maxtempos[i+1]-maxtempos[i]

print("-----------------Alinea {} -------------------".format("b"))
plt.plot(t,angulo)
plt.xlabel('t(s)') 
plt.ylabel('x')

print('A=',maxangtotal/countmax,"T=",tempototal/(countmax-1))

plt.show()