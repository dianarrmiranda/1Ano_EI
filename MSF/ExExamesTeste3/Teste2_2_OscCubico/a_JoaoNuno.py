import matplotlib.pyplot as plt
import numpy as np
#   Faça o diagrama de energia desta energia potencial.

k=1.2
alpha= -0.01
ti =0
tf=10
dt = 0.01
n = int((tf-ti) / dt)  
zeros = np.empty(n)

for i in range(n-1):
    zeros[i] = 2

zeros[n-1] = 2
 
x = np.linspace(-2, 2,n)  
Ep = 0.5 * k*(x**2) + alpha* (x**3)
plt.plot(x,zeros)
plt.plot(x, Ep)    
plt.xlabel("x (m)")
plt.ylabel("Ep (J)")
plt.title("Energia Potencial")
plt.grid()
plt.show()