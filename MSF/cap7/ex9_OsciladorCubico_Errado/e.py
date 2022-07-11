import matplotlib.pyplot as plt
import numpy as np

#Calcule a lei do movimento, quando a posição inicial for 2.9 m e a velocidade inicial
#nula? Quanto é a energia mecânica? Entre que limites se efetua o movimento e a
#frequência do movimento?

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

# máximo pelo polinómio de Lagrange
def maximo(xm1,xm2,xm3,ym1,ym2,ym3):  
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


#a) Faça o diagrama de energia desta energia potencial. Qual o movimento quando a energia total for menor que 1 J? 

m = 1
k = 1
g=9.8

xeq = 0
alfa = -0.01

t0 = 0
tf =40
dt = 0.001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)
Ep = np.empty(n)
Ec = np.empty(n)
EM = np.empty(n)

em = 1

x[0] =2.9
v[0] = 0


a[0] = -k/m*x[0] - (3*alfa*(x[0]**2))/m

for i in range(n-1):   
    a[i+1] = -k/m*x[i] - (3*alfa*(x[i]**2))/m
    v[i+1] = v[i] +a[i+1]*dt #a[i+1] - euler cromer
    x[i+1] = x[i] +v[i+1]*dt
    
    Ep[i] = 0.5*k*(x[i]**2) + alfa*(x[i]**3)
    Ec[i] = m*0.5*v[i]**2
    EM[i] = Ec[i] + Ep[i]
    
Ep[n-1] = 0.5*k*(x[n-1]**2) + alfa*(x[n-1]**3)
Ec [n-1]= m*0.5*v[n-1]**2
EM[n-1] = Ec[n-1] + Ep[n-1]

## Cálculo dos máximos com recurso ao Polinómio de Lagrange. Permite calcular amplitude e mais tarde T
maxGraficos = []

for i in range(n-1):
    if x[i-1] < x[i] and  x[i+1] < x[i]:
        maxt, maxx = maximo(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])
        if len(maxGraficos) == 0:
            print("O máximo do movimento é {:.2f} m.".format((maxx)))
        maxGraficos.append((maxt,maxx))

for i in range(n-1):
    if abs(x[i-1]) < abs(x[i]) and  abs(x[i+1]) < abs(x[i]):
        maxt, minx = maximo(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])
        maxx=1.30
        if minx != maxx:
            print("O minimo do movimento é {:.2f} m.".format(minx))
            break
        else:
            continue
        
## Cálculo do período T
T = []
tAnt = 0
tNovo = 0
i = 0

for (tmax,max) in maxGraficos:
    i += 1
    if i > 1:
        T.append(abs(tmax-tNovo))
        tNovo, tAnt = tmax, tNovo
    else:
        tNovo, tAnt = tmax, tNovo

periodo = sum(T)/len(T)
print("O período do movimento é {:.3f}.".format(periodo))

print(periodo/dt)
a,b = abfourier(t,x,0,4761,1)
print("Os coeficientes de Fourier são a = {:.2f}, b = {:.2f}.".format(abs(a),abs(b)))

print("Energia mecânica: ", EM)	
plt.plot(t,x)
plt.xlabel("x (m)")
plt.ylabel("t (s)")
plt.show()

