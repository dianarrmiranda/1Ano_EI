#b) Apresente as medições num gráfico log-log. Qual a dependência entre as quantidade
#período e massa? 

import numpy as np
import matplotlib.pyplot as plt

#a) Apresente estas medições num gráfico
M = np.array([0.15, 0.20,0.16,0.11,0.25,0.32,0.40,0.45,0.50,0.55])
T = np.array([1.21,1.40,1.26,1.05,1.60,1.78,2.00,2.11,2.22,2.33])

x = M
y = T

logx = np.log(x)
logy = np.log(y)

m = np.polyfit(logx,logy,1)[0]
b = np.polyfit(logx,logy,1)[1]

xmax=np.max(logx)*0.9
xmin=np.min(logx)*1.1
x = np.linspace(xmin, xmax, 100)

plt.scatter(logx,logy)
plt.plot(x,m*x+b)
plt.xlabel("Log(M)")
plt.ylabel("Log(T)")
plt.show()