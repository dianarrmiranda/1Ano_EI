#c) Em que instante volta a passar pela posição inicial, no caso da alínea a)? Qual a
#velocidade nesse instante?

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

#Volta ao solo quando y = 0
tpi = vi/4.9
#velcidade nesse instante
#v= gt + v0
vpi= g*tpi + vi

print('Volta a passar pelomposição inical em {:.2f}s'.format(tpi))
print('Velociade nesse instante {:.2f}m/s'.format(vpi))

plt.xlabel('tempo (s)')
plt.ylabel('X (m)')
plt.plot(t, y, label='Posição sem resistência do ar, dt = 0.001')
plt.plot(tpi, 0, 'x', label='Volta a passar pela posição inicial')
plt.legend()
plt.show()