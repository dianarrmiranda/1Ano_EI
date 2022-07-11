#Faça o gráfico da lei do movimento 𝑦(𝑡) de 0 a 4.0 s. 

import numpy as np
import matplotlib.pyplot as plt

#Alinea A

#input
vt = 6.8 #velocidade terminal (é o declive da reta que o gráfico forma)
g = -9.8 #gravidade
t = np.linspace(0, 4, 100)  #(tempo inicial, tempo final, número de pontos)

log = np.log(np.cosh(g*t/vt)) #logaritimo

yt = ((vt**2)/g)*log #Lei do movimento

plt.xlabel("tempo(s)")
plt.ylabel("y(m)")
plt.plot(t, yt, label = "y(t) do volante")
plt.legend()
plt.title("Gráfico da lei do movimento y(t) de 0 a 4.0 s") #Queda do volante com vy(0) = 0 

plt.show()