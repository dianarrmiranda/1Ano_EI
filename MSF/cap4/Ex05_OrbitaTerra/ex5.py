import numpy as np
import matplotlib.pyplot as plt

x0 = 1
y0 = 0

vx0 = 0
vy0 = 2*np.pi

G = 4*(np.pi)**2

## Passo temporal para o Método de Euler
t0 = 0.00 ##tempo inicial
tf = 5 ##tempo final
dt = 0.001 ##passo temporal
n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

## NOTA: Vx é constante s/ resistência do ar (igual a Vx0)
ax = np.empty(n)
ay = np.empty(n)
vx = np.empty(n)
vy = np.empty(n)
x = np.empty(n)
y = np.empty(n)

vy[0] = vy0
vx[0] = vx0

x[0] = x0
y[0] = y0

## Ciclo que implementa o Método de Euler-Cromer, e atualiza o array tempo para podemos fazer um plot
for i in range(n-1):
    r = np.sqrt(x[i]**2 + y[i]**2)

    ax[i]=-G*x[i]/r**3
    ay[i]=-G*y[i]/r**3

    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] + ax[i]*dt

    x[i+1] = x[i] + vx[i+1]*dt
    y[i+1] = y[i] + vy[i+1]*dt

plt.plot(x,y)
plt.show()

#a) A órbita da Terra à volta do sol é fechada? Consegue obter elipses? - Não
#b) Consegue órbitas fechadas? São elipses? Concordam com as leis de Kepler? - (Código acima) Sim, são e sim concordam com as leis de kepler.
#c) Encontre o erro de truncatura deste método de Euler-Cromer. - Erro linearmente proporcional a dt

