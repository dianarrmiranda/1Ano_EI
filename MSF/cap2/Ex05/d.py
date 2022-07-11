#a) c) Determine a lei do movimento 𝑦(𝑡), usando o método de Euler. Faça o gráfico da
#posição em função do tempo.


import matplotlib.pyplot as plt
import numpy as np

y = np.array([0,0.61,1.22,1.52,1.83,2.00,2.13,2.44,2.74,3.00,4.00,5.00,6.00,7.00,8.50,9.50])
t = np.array([0,0.347, 0.470, 0.519, 0.582, 0.650, 0.674, 0.717, 0.766, 0.823,0.870, 1.031, 1.193, 1.354, 1.501, 1.726, 1.873])

v0 = 0

g = 9.80 #aceleração gravitica

# Passo temporal para o Método de Euler
dt = 0.001 #passo temporal
n = y.size #Nº de passos a realizar

# Resistência do Ar
vt = 6.80
D = g/vt**2

# Criação de arrays de velocidade, posição e tempo com N lugares, para os N passos,
#  preenchidos por 0's. Caso a velocidade ou posição inicial seja diferente de 0, temos que fazer a correção.
vy = np.empty(n)
ay = np.empty(n)

vy[0] = v0
ay[0] = 0

# Ciclo que implementa o Método de Euler, e atualiza o array tempo para podemos fazer um plot
for i in range(n):
    vv = np.abs(vy[i])
    ay[i] = g - D*vy[i]*vv
    vy[i] = vy[i] + ay[i]*dt

plt.plot(t,y, label= "met Euler dt = 0.001s")
plt.xlabel('t (s)')
plt.ylabel('y(t) (m)')

plt.title("Queda do volante vt = 6.80 m/s.")
plt.legend()
plt.show()