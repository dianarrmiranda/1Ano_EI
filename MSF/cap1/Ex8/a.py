import numpy as np
import matplotlib.pyplot as plt

#a) Apresente estas medições num gráfico. A analisar o gráfico, a relação entre a energia
#emitida e a temperatura é linear?

T= [200, 300 , 400, 500, 600, 700, 800, 900, 1000, 1100]
E = [0.6950, 4.363, 15.53, 38.74, 75.08, 125.2, 257.9, 344.1, 557, 690.7]

x=T
y=E

plt.scatter(x,y)
plt.xlabel("T (k)")
plt.ylabel("E (j)")
plt.show()

#RESOSTA: A relação entre a energia emitida e a temperatura não é linear 