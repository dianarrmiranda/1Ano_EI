import matplotlib.pyplot as plt
import numpy as np

#a) Faça o diagrama de energia desta energia potencial. Qual o movimento quando a energia total for menor que 1 J? 

m = 1
k = 1
g=9.8

xeq = 1.5

t0 = 0
tf =400
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

em = 1 

x[0] = np.sqrt(np.sqrt(2*em/k)+xeq**2)
v[0] = 0

a[0] = -k/m*x[0]

for i in range(n-1):   
    a[i+1] = -2*k/m*(x[i]**2-xeq**2)*x[i]
    v[i+1] = v[i] +a[i+1]*dt #a[i+1] - euler cromer
    x[i+1] = x[i] +v[i+1]*dt
    Ep[i] = 0.5*k*(x[i]**2-xeq**2)**2
    Ec[i] = m*0.5*v[i]**2
    EM[i] = Ec[i] + Ep[i]
    
Ep[n-1] = 0.5*k*(x[n-1]**2-xeq**2)**2
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
