#b) Qual a altura máxima e o instante em que ocorre, no caso da alínea a)?

import matplotlib.pyplot as plt
import numpy as np

vi = 10 # m/s
dt = 0.001
t0 = 0
tf = 2.2+dt
g = -9.8 #m/s^2 
n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)
y = vi*t - 4.9*t**2

#Altura máxima é quando v = 0
#v= gt + v0
tmax = -vi/g

ymax = vi*tmax - 4.9*tmax**2

print('Atinge a altura máxima de {:.2f}m em {:.2f}s'.format(ymax, tmax))

plt.xlabel('tempo (s)')
plt.ylabel('X (m)')
plt.plot(t, y, label='Posição sem resistência do ar, dt = 0.001')
plt.plot(tmax, ymax, 'x', label='Altura máxima')
plt.legend()
plt.show()