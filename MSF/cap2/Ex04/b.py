#b) Determine a velocidade instantânea, usando o método de Euler. Faça o gráfico da
#velocidade em função do tempo. Qual a velocidade do volante (em km/h) ao fim de 1s?

from re import I
import numpy as np
import matplotlib.pyplot as plt

# DADOS
g = 9.8
v0 = 200 / 3.6
vTerminal = 6.80
y0 = 0
vy0 = v0

dt = 0.01
ti = 0
tf = 5
n = int((tf - ti) / dt)

## Criação de arrays de velocidade, posição e tempo com N lugares, para os N passos,
#  preenchidos por 0's. Caso a velocidade ou posição inicial seja diferente de 0, temos que fazer a correção.
t = np.empty(n)
vy = np.empty(n)
ay = np.empty(n)
y = np.empty(n)

D = g / vTerminal ** 2
t[0] = ti
vy[0] = v0  # sentido do eixo de cima para baixo
y[0] = y0
ay[0] = g - D * abs(vy[0]) * vy[0]

#Ciclo que implementa o Método de Euler, e atualiza o array tempo para podemos fazer um plot
for i in range(n-1):
    # tempos
    t[i + 1] = t[i] + dt

    # aceleracoes
    ay[i+1] = g - D * abs(vy[i]) * vy[i]

    # velocidades
    vy[i + 1] = vy[i] + ay[i] * dt

    # posicoes
    y[i + 1] = y[i] + vy[i] * dt
    
for i in range(n-1):
    if (t[i]>(1-dt) and t[i+1] <(1+dt)):
        print("dt, t, vy = ", dt, t[i+1], vy[i+1])
        
        print("A posição em 1s é {:.1f} km/h".format(vy[i+1]*3.6))
        plt.plot(t[i+1],vy[i+1], "o", label="y(t) em 1s")
        break
    
plt.plot(t,vy, label= "met Euler dt = 0.01s")
plt.xlabel('t (s)')
plt.ylabel('vy(t) (m/s)')

plt.title("Queda do volante vt = 6.80 m/s.")
plt.legend()
plt.show()