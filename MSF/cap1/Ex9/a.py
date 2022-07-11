#a) Apresente estas medições num gráfico. A analisar o gráfico, a relação entre a
#atividade e o tempo é linear?

import matplotlib.pyplot as plt
import numpy as np

R = [9.676 , 6.355, 4.261, 2.729, 1.862, 1.184, 0.7680, 0.4883, 0.3461, 0.2119]
t = [0,5,10,15,20,25,30,35,40,45]

x = t
y = R

plt.plot(x,y,"o")
plt.xlabel("Tempo (dias)")
plt.ylabel("Radioatividade (mCi)")
plt.show()
# Não, a relação entre os dados não é linear.
