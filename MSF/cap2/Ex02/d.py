#d) Mostre que a aceleração 𝑎𝑦(𝑡) = 𝑔 −𝑔/𝑣t^2*|𝑣𝑦|*𝑣𝑦 é equivalente à calculada na alínea anterior.

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym #calculo simbólico

#Alinea d

v = sym.Symbol('v')
D = sym.Symbol('D')
vt = sym.Symbol('vt')
t = sym.Symbol('t')
g = sym.Symbol('g')
a = sym.Symbol('a')
aS = sym.Symbol('as')

vt = 6.8 #velocidade terminal (é o declive da reta que o gráfico forma)
g = 9.8 #gravidade
t = np.linspace(0, 4, 100)  #(tempo inicial, tempo final, número de pontos)

#Calcular valor acelaração
vi = vt*np.tanh(g*t/vt) #vi
acel = g-(g/(vt**2)) * vi * abs(vi)

plt.plot(t, acel)
plt.xlabel("t (s)")
plt.ylabel("y (m)")
plt.title("Gráfico da acelaração em função do tempo de 0 a 4 s")
plt.show()

