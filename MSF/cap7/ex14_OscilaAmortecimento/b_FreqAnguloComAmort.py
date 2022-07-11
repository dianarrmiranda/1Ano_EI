import matplotlib.pyplot as plt
import numpy as np

#b) A frequência angular da oscilação considerando agora que o amortecimento afeta a
#oscilação.

m=1 
k=1
wf=1.0
fo=7.5
b=0.16
tf=300
ti=0    
dt= 0.0001
n=int((tf-ti)/dt)
t=np.linspace(ti,n*dt,n)


x0=2
v0=3
a0=0

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)

x[0]=x0
v[0]=v0

for i in range (n-1):
    fext=fo*np.cos(wf*t[i])
    fem=-b*v[i]
    fx=-k*x[i]
    a[i]=(fext+fem+fx)/m
    v[i+1]=v[i]+a[i]*dt
    x[i+1] =x[i]+v[i+1]*dt

print("-----------------Alinea (b)-------------------")

print("Frenquencia Angular {:.4f} rad/s".format(np.sqrt(k/m - (b/(2*m))**2)))
plt.plot(t,x)
plt.xlabel('t(s)') 
plt.ylabel('x(m)')
plt.grid(True)
plt.show()


