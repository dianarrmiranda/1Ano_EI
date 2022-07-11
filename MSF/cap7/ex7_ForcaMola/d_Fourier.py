
import matplotlib.pyplot as plt
import numpy as np

def graficoBarras(ii,lst,xlabel,ylabel):
    plt.figure()
    plt.xlabel(xlabel) 
    plt.ylabel(ylabel)
    plt.bar(ii,np.abs(lst))
    plt.grid(True)
    plt.show()
    
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

def abfourier(tp,xp,it0,it1,nf):
#
# cálculo dos coeficientes de Fourier a_nf e b_nf
#       a_nf = 2/T integral ( xp cos( nf w) ) dt   entre tp(it0) e tp(it1)
#       b_nf = 2/T integral ( xp sin( nf w) ) dt   entre tp(it0) e tp(it1)    
# integracao numerica pela aproximação trapezoidal
# input: matrizes tempo tp   (abcissas)
#                 posição xp (ordenadas) 
#       indices inicial it0
#               final   it1  (ao fim de um período)   
#       nf índice de Fourier
# output: af_bf e bf_nf  
# 
    dt=tp[1]-tp[0]
    per=tp[it1]-tp[it0]
    ome=2*np.pi/per

    s1=xp[it0]*np.cos(nf*ome*tp[it0])
    s2=xp[it1]*np.cos(nf*ome*tp[it1])
    st=xp[it0+1:it1]*np.cos(nf*ome*tp[it0+1:it1])
    soma=np.sum(st)
    
    q1=xp[it0]*np.sin(nf*ome*tp[it0])
    q2=xp[it1]*np.sin(nf*ome*tp[it1])
    qt=xp[it0+1:it1]*np.sin(nf*ome*tp[it0+1:it1])
    somq=np.sum(qt)
    
    intega=((s1+s2)/2+soma)*dt
    af=2/per*intega
    integq=((q1+q2)/2+somq)*dt
    bf=2/per*integq
    return af,bf

#--------------------------------------------------------------------------------#

ind = np.transpose([0 for i in range(1000)])

afo = np.zeros(15) #número de frequências
bfo  = np.zeros(15)

m = 1
k = 1
g=9.8
w=np.sqrt(k/m)

t0 = 0
tf =30
dt = 0.001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)

energia=np.empty(n)

x[0] = 4
v[0] = 0

a[0] = 0

countMax=0
maxxtotal = 0
maxTempos = []
tempoTotal = 0



for i in range(n-1):   
    a[i]=-k *x[i]/m
    v[i+1]=v[i]+a[i]*dt
    x[i+1] =x[i]+v[i+1]*dt
    
    energia[i]=0.5*x[i]**2+ 0.5*v[i]**2  #Em = U + Ec   U = 0.5kx^2   Ec = 0.5mv^2
    fx=-k *x[i]


    if i>1 and x[i-1] < x[i] and  x[i+1] < x[i]:
        maxt, maxx=maximo(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])
        maxxtotal +=maxx
        countMax+=1
        maxTempos.append(maxt)
        ind[countMax]=int(i) #nota que tem de ser inteiro
            
t0 = ind[countMax-1]
t1 = ind[countMax]

for i in range(15):
    af, bf=abfourier(t,x,t0,t1,i)
    afo[i] = af
    bfo[i] = bf

li=np.linspace(0,14,15)
print("-----------------Alinea (c)-------------------")
graficoBarras(li,afo,'n','| a_n |')
graficoBarras(li,bfo,'n','| b_n |')

#𝑥(𝑡) = 𝑎1 cos(𝜔𝑡) + 0
