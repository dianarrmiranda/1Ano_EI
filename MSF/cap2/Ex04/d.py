#d) Determine a lei do movimento 𝑦(𝑡), usando o método de Euler. Faça o gráfico da
#posição em função do tempo. Em quanto tempo percorre 4 m?
#Note: Teste o programa para o caso 𝑣𝑦(0) = 0, em que se conhece a solução exata.

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
    if ((4-0.03) < y[i] < (4+0.03)):
        print("dt, t, y = ", dt, t[i], y[i])
        print("Percorre 4m em {:.2f} s".format(t[i]))
        plt.plot(t[i],y[i], "o", label="t quando y(t) = 4m")
        break
    
plt.plot(t,y)
plt.xlabel('t (s)')
plt.ylabel('y(t) (m)')
plt.title("Queda do volante vt = 6.80 m/s.")
plt.legend()
plt.show()