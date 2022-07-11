#c) Determine a aceleração instantânea em função do tempo, usando cálculo simbólico.
#Faça o gráfico da aceleração em função do tempo de 0 a 4 s, usando o pacote matplotlib.

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym #calculo simbólico

#Alinea c

v = sym.Symbol('v')
D = sym.Symbol('D')
vt = sym.Symbol('vt')
t = sym.Symbol('t')
g = sym.Symbol('g')
a = sym.Symbol('a')
aS = sym.Symbol('as')

#Calcular derivadas
D = sym.Derivative(vt*sym.tanh(g*t/vt) , t, evaluate = True) #expressão, derivar em ordem a x (Derivar a formula da acelaração)
print('dy/dt = ', D) #Derivada
a = sym.simplify(D)
print('dy/dt = ', a) #Derivada simplificada

vt = 6.8 #velocidade terminal (é o declive da reta que o gráfico forma)
g = 9.8 #gravidade
t = np.linspace(0, 4, 100)  #(tempo inicial, tempo final, número de pontos)

#Calcular valor acelaração
acel = g/np.cosh(g*t/vt)**2

plt.plot(t, acel)
plt.xlabel("t (s)")
plt.ylabel("y (m)")
plt.title("Gráfico da acelaração em função do tempo de 0 a 4 s")
plt.show()
