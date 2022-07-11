#c) Repita a alínea anterior, com um passo 10 vezes menor.


import numpy as np
import matplotlib.pyplot as plt

t0 = 0 #s
tf = 4 #s
g = 9.8 #m/s g = aceleracao

dt = 0.001 #s

n = int((tf-t0)/dt)

t = np.linspace(0,4,n)
v = np.empty(n)
v0 = v[0]

for i in range(n-1):
    v[i+1] = v[i] + g * dt
    
    
plt.plot(t,v, "o", label= "v(t) do objeto")
plt.xlabel('t (s)')
plt.ylabel('v (m/s)')

for i in range(n-1):
    if (t[i]>(3-dt) and t[i+1] <(3+dt)):
        print("dt, t, v = ", dt, t[i+1], v[i+1])
        print("A velocidade em 3s é {:.1f} s".format(v[i+1]))
        plt.plot(t[i+1],v[i+1], "o", label="v(t) em 3s")
        break


plt.title("Gráfico da lei do movimento v(t) de 0 a 4.0 s")
plt.legend()
plt.show()
