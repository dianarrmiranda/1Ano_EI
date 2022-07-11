import matplotlib.pyplot as plt
import numpy as np

#a) Faça o diagrama de energia desta energia potencial. Qual o movimento quando a energia total for menor que 1 J? 

m = 1
k = 1
g=9.8

xeq = 0
alfa = -0.01

t0 = 0
tf =100
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

x[0] = np.sqrt(np.sqrt(2*em/k)+xeq**2)
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


plt.plot(x,Ep)
plt.xlabel("x (m)")
plt.ylabel("EP (J)")
plt.title("Energia Potencial, quando a energia total for 1J")
plt.show()

plt.plot(x,EM)
plt.xlabel("x (m)")
plt.ylabel("EM (J)")
plt.title("Energia Mecânica, quando a energia total for 1J")
plt.show()
