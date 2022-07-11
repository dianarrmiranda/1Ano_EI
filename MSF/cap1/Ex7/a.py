#a) Apresente estas medições num gráfico. A analisar o gráfico, a relação ente o período de oscilação e a massa é linear?

import numpy as np
import matplotlib.pyplot as plt

#a) Apresente estas medições num gráfico
M = np.array([0.15, 0.20,0.16,0.11,0.25,0.32,0.40,0.45,0.50,0.55])
T = np.array([1.21,1.40,1.26,1.05,1.60,1.78,2.00,2.11,2.22,2.33])

x = M
y = T
plt.scatter(x,y)
plt.xlabel("M (Kg)")
plt.ylabel("T (s)")
plt.show()

# RESPOSTA: Não é linear.
