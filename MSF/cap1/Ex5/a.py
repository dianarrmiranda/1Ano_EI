import numpy as np
import matplotlib.pyplot as plt

#a) Comece por representar os dados experimentais num gráfico
L=np.array([222.0,207.5,194,171.5,153.0,133.0,113.0,92.0])
X=np.array([2.3,2.2,2.0,1.8,1.6,1.4,1.2,1.0])

x =L 
y = X
plt.scatter(x, y)
plt.xlabel("L (cm)")
plt.ylabel("X (cm)")
plt.show()