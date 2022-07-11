import matplotlib.pyplot as plt
import numpy as np

#f) Faça a análise de Fourier das solução encontrada na alínea a)

def graficoBarras(ii,lst,xlabel,ylabel):
    plt.figure()
    plt.xlabel(xlabel) 
    plt.ylabel(ylabel)
    plt.bar(ii,np.abs(lst))
    plt.grid(True)
    plt.show()
    
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

#------------------------------------------------------------------------------

ind = np.transpose([0 for i in range(1000)])

m = 1
k = 1

xeq =2

x0 = 3 
v0 = 0


t0 = 0
tf =30
dt = 0.0001

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
countMax = 0

for i in range(n-1):  
    
    v[i+1]=v[i]+a[i]*dt
    x[i+1] =x[i]+v[i+1]*dt

    if x[0]<0:
        a[i+1]= -x[i+1] - xeq
    else:
        a[i+1]= -x[i+1] + xeq
    
    if (t[i]>0 and x[i-1]<x[i]>x[i+1] and i>0 ):
        countMax = countMax+1
        ind[countMax] = int(i)
    
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

print("-----------------Alinea (f)-------------------")


#15 é um numero arbitario e calculo as 5 primeiras frequencias
afo=np.zeros(15)
bfo=np.zeros(15)
    
li=np.linspace(0,14,15)

t0 = ind[countMax-1]
t1 = ind[countMax]

for i in range(15):
    af, bf = abfourier(t,x,t0,t1,i)
    afo[i]= af
    bfo[i]= bf
    
#print("afo= ", i, af, bf, np.sqrt(af**2 + bf**2))
graficoBarras(li,afo,'n','| a_n |')
graficoBarras(li,bfo,'n','| b_n |')

