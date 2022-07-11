
import numpy as np
import matplotlib.pyplot as plt

#MAIN
#------------------------------------
# Gravidade
g = 9.8

# Massa
m = 0.5

# k e b
k = 1.8
b = 0.9

# Tempo inicial e final
t0 = 0
tf = 15

# Velocidade terminal
# vtx = 6.8

# Posição e Velocidade inicial
xeq = 0
x0 =2.5
vx0 = 3

# dt incremento do tempo e n numero de intervalos
dt = 0.001
n = int((tf - t0) / dt)

# Vetor tempo (n+1 para garantir que nao falta o ultimo dado (Ex: t[10]))
t = np.linspace(t0, tf, n + 1)

# Vetor velocidade (empty e não zeros para não alterar
# muito o resultado se faltar analisar um dado)
x = np.empty(n + 1)
vx = np.empty(n + 1)
ax = np.empty(n + 1)

Ep = np.empty(n+1)
Ec = np.empty(n+1)
Em = np.empty(n+1)

xrk4 = np.empty(n + 1)
vxrk4 = np.empty(n + 1)

# Introduzir x0 e v0 nos vetores da posição e velocidade
x[0] = x0
vx[0] = vx0
# xrk4[0] = xx0
# vxrk4[0] = vx0

#Euler-crommer
for i in range(n):
    ax[i]=-(k/m)*x[i]-4*(b/m)*x[i]**3
    vx[i + 1] = vx[i] + ax[i] * dt
    x[i + 1] = x[i] + vx[i+1] * dt
    
    Ep[i]= 0.5*k*x[i]**2 + b*x[i]**4
    Ec[i]= 0.5*m*vx[i]**2
    
    Em[i] = Ec[i] + Ep[i]

#LAST VALUES
Ep[n]= 0.5*k*x[n]**2 + b*x[n]**4
Ec[n]= 0.5*m*vx[n]**2
 
plt.plot(x, Ep)    
plt.xlabel("x (m)")
plt.ylabel("Ep (J)")
plt.title("Energia Potencial")
plt.grid()
plt.show()