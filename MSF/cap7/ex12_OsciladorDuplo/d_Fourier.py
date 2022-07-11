import matplotlib.pyplot as plt
import numpy as np

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

#d) Faça a análise de Fourier das solução encontrada na alínea b)

ind = np.transpose([0 for i in range(1000)])

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

em = 0.75 #j

x[0] = np.sqrt(np.sqrt(2*em/k)+xeq**2)
v[0] = 0

a[0] = -k/m*x[0]

countMax = 0 

for i in range(n-1):   
    a[i+1] = -2*k/m*(x[i]**2-xeq**2)*x[i]
    v[i+1] = v[i] +a[i+1]*dt #a[i+1] - euler cromer
    x[i+1] = x[i] +v[i+1]*dt
    Ep[i] = 0.5*k*(x[i]**2-xeq**2)**2
    Ec[i] = m*0.5*v[i]**2
    EM[i] = Ec[i] + Ep[i]

    if (t[i]>0 and x[i-1]<x[i]>x[i+1] and i>0 ):
        countMax = countMax+1
        ind[countMax] = int(i)
    
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