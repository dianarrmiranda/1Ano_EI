#b) Determine a velocidade instantânea em função do tempo, usando cálculo simbólico.
#Faça o gráfico da velocidade em função do tempo de 0 a 4 s, usando o pacote matplotlib.

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym #calculo simbólico

#Alinea b

v = sym.Symbol('v')
D = sym.Symbol('D')
vt = sym.Symbol('vt')
t = sym.Symbol('t')
g = sym.Symbol('g')

#Calcular derivadas
D = sym.Derivative(((vt**2)/g)*(sym.log(sym.cosh(g*t/vt))) , t, evaluate = True) #expressão, derivar em ordem a x
print('dy/dt = ', D) #Derivada
v = sym.simplify(D)
print('dy/dt = ', v) #Derivada simplificada

vt = 6.8 #velocidade terminal (é o declive da reta que o gráfico forma)
g = -9.8 #gravidade
t = np.linspace(0, 4, 100)  #(tempo inicial, tempo final, número de pontos)

#Calcular valor v
vi = vt*np.tanh(g*t/vt)


plt.plot(t, vi)
plt.xlabel("t (s)")
plt.ylabel("y (m)")
plt.title("Gráfico da velocidade em função do tempo de 0 a 4 s")
plt.show()
