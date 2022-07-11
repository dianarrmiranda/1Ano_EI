#h) Calcule novamente a posição no instante 2 s, com o passo 10 vezes menor. Faça o
#gráfico do desvio do valor aproximado com o valor exato em função do passo.
#Como varia o erro com o passo?

import math
import numpy as np
import matplotlib.pyplot as plt

a = 9.8
tf = 4
t0 = 0
dt = [0.01, 0.001, 0.0001, 0.00001]

valort = (1/2)*a*(2**2) #Valor teórico

desvio = np.empty(len(dt))

for j in range (len(dt)):
    n = int((tf - t0)/dt[j])
    t = np.linspace(t0, tf, n+1)
    v = np.empty(n+1)
    v[0] = 0
    y = np.empty(n+1)
    y[0] = 0
    for i in range(n):
        v[i+1] = v[i] + a * dt[j]
        y[i+1] = y[i] + v[i] * dt[j]
    
    for i in range(n):
        if (t[i] > (2-dt[j]) and t[i] < (2+dt[j])):
            print("dt, t, y =", dt[j], t[i], y[i])
            desvio[j] = abs(valort - y[i]) 
            plt.plot(dt[j], desvio[j], "ro")


plt.xlabel("dt (s)")
plt.ylabel("desvio (m)")
plt.plot(dt, desvio)
plt.legend()
plt.show()

#RESPOSTA: O erro vai diminuindo conforme o passo diminui.
#desvio é proporcional ao passo 
