#a) Calcule a expressão da velocidade terminal em função de 𝐶.
#vt = g/C

#b) Determine a velocidade instantânea, usando o método de Euler. Faça o gráfico da
#velocidade em função do tempo.

import matplotlib.pyplot as plt
import numpy as np

x0 = 0
v0 = 0

g = 9.80 #aceleração gravitica

# Passo temporal para o Método de Euler
dt = 0.001 #passo temporal
t0 = 0.00 #tempo inicial
tf = 5.00 #tempo final
n = np.int((tf-t0)/dt) #Nº de passos a realizar

# Resistência do Ar
vt = 6.80
D = g/vt**2

# Criação de arrays de velocidade, posição e tempo com N lugares, para os N passos,
#  preenchidos por 0's. Caso a velocidade ou posição inicial seja diferente de 0, temos que fazer a correção.
t = np.empty(n)
vy = np.empty(n)
ay = np.empty(n)
y = np.empty(n)

vy[0] = v0
y[0] = x0
ay[0] = 0
t[0] = t0

# Ciclo que implementa o Método de Euler, e atualiza o array tempo para podemos fazer um plot
for i in range(n-1):
    t[i+1] = t[i] + dt

    vv = np.abs(vy[i])
    ay[i+1] = g - D*vy[i]*vv

    vy[i+1] = vy[i] + ay[i]*dt
    y[i+1] = y[i] + vy[i]*dt

plt.plot(t,vy, label= "met Euler dt = 0.001s")
plt.xlabel('t (s)')
plt.ylabel('vy(t) (m/s)')

plt.title("Queda do volante vt = 6.80 m/s.")
plt.legend()
plt.show()
    