#a) ) Faça o gráfico da lei do movimento do carro A e do carro patrulha, 𝑥 = 𝑥(𝑡)

import numpy as np
import matplotlib.pyplot as plt

#input
x0 = 0  #posição inicial
v0policia = 0 #Velocidade inical da polícia

v0_kmh = 70 #Velocidade inical da carro
v0 = 70/3.6 #metro por segundo m/s
a = 2.0

t = np.linspace(0, 30, 100)  #(tempo inicial, tempo final, número de pontos)

xc = v0*t #posição em função do tempo do carro

xp = x0 + v0policia*t + (1/2)*a*t**2 #posição em função do tempo da polícia 


plt.xlabel("tempo(s)")
plt.ylabel("x(m)")
plt.plot(t, xc, label = "x(t) Carro")
plt.plot(t, xp, label = "x(t) Carro Polícia")
plt.legend()
plt.title("Dois Carros")

plt.show()