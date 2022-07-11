import matplotlib.pyplot as plt
import numpy as np


#a) Faça o diagrama de energia desta energia potencial. Qual o movimento quando a energia total for menor que 4 J?

m = 0.5
k = 1.8
g=9.8

xeq = 0

beta = 0.9 #N/m^3

t0 = 0
tf =200
dt = 0.001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)
Ep = np.empty(n)
Ec = np.empty(n)
EM = np.empty(n)
zeros = np.empty(n)
em = 4

x[0] = 0
v[0] = np.sqrt(2*em/m)

a[0] = -k/m*x[0] - (4*beta*(x[0]**3))/m

for i in range(n-1):   
    a[i+1] = -(k/m)*x[i] - (4*beta*(x[i]**3))/m
    v[i+1] = v[i] +a[i+1]*dt #a[i+1] - euler cromer
    x[i+1] = x[i] +v[i+1]*dt
    
    Ep[i] = 0.5*k*(x[i]**2) + beta*(x[i]**4)
    EM[i] = 0.5*m*v[i]**2 + Ep[i]
    
    zeros[i] = 4
    
Ep[n-1] = 0.5*k*(x[n-1]**2) + beta*(x[n-1]**4)
EM[n-1] = 0.5*m*v[n-1]**2 + Ep[n-1]

zeros[n-1] = 4


plt.plot(x,Ep)
plt.plot(x,zeros)
plt.xlabel("x (m)")
plt.ylabel("EP (J)")
plt.title("Energia Potencial, quando a energia total for 4J")
plt.show()

plt.plot(x,EM)
plt.xlabel("x (m)")
plt.ylabel("EM (J)")
plt.title("Energia Mecânica, quando a energia total for 4J")
plt.show()

#Energia Potencial não simétrica 
#Corpo com energia Energia <= 2J
#Momento periódico:
#Corpo nula entre 2 extremos não simétricos em que a posição média não coincide
#com a posição de equilíbrio, ou, a energia potencial na zona positiva de x é menor
#que na zona negativa de x. O que faz o corpo passar mais tempo na parte positiva do eixo.