#a) Encontre analiticamente a lei do movimento 𝑦 = 𝑦(𝑡), se não considerar a resistência 
# do ar. Faça o gráfico de y em função do tempo.

import matplotlib.pyplot as plt
import numpy as np


#Alinea A

vi = 10 # m/s
dt = 0.001
t0 = 0
tf = 2.2+dt
g = -9.8 #m/s^2 
n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)
y = vi*t - 4.9*t**2


plt.xlabel('tempo (s)')
plt.ylabel('X (m)')
plt.plot(t, y, label='Posição sem resistência do ar, dt = 0.001')
plt.legend()

plt.show()