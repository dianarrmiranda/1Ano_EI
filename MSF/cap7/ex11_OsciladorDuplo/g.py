import matplotlib.pyplot as plt
import numpy as np

# d) Analise fourier alinea c)

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

m = 1
k = 1

xeq =2
ep = 0.75 #j

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

maxxtotal=0
countmax=0
maxtempos=[]
tempototal=0

ind = np.transpose([0 for i in range(1000)])

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

## Cálculo dos máximos com recurso ao Polinómio de Lagrange. Permite calcular amplitude e mais tarde T
maxGraficos = []
for i in range(n-1):
    if x[i-1] < x[i] and  x[i+1] < x[i]:
        maxt, maxx = maxminv(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])
        if len(maxGraficos) == 0:
            print("O máximo do movimento é {:.3f} m.".format(abs(maxx)))
        maxGraficos.append((maxt,maxx))

for i in range(n-1):
    if x[i-1] > x[i] and  x[i+1] > x[i]:
        maxt, minx = maxminv(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])
        if minx != maxx:
            print("O minimo do movimento é {:.3f} m.".format(minx))
            break
        else:
            continue

print("Frequencia {:.3f} Hz.".format((countmax-1)/tempototal))

plt.figure()
plt.plot(t,x)
plt.ylabel('x (m)')
plt.xlabel( 't (s)' )
plt.grid()
plt.show()

print("-----------------Alinea-------------------")

li=np.linspace(0,14,15)

#15 é um numero arbitario e calculo as 5 primeiras frequencias
afo=np.zeros(15)
bfo=np.zeros(15)

for i in range(15):
    af, bf = abfourier(t,x,t0,t1,i)
    afo[i]= af
    bfo[i]= bf

#print("afo= ", i, af, bf, np.sqrt(af**2 + bf**2))

graficoBarras(li,afo,'n','| a_n |')
graficoBarras(li,bfo,'n','| b_n |')
