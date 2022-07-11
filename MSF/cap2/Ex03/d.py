#d) Compare o resultado obtido em b) e c) com o resultado exato. Que conclui?

import numpy as np
import matplotlib.pyplot as plt

t0 = 0 #s
tf = 4 #s
g = 9.8 #m/s g = aceleracao

dt = 0.001 #s

#Alinea d
v3 = g*3

print("Com dt=0.01 temos v(3) = 29.4 s")
print("Com dt=0.001 temos v(3) = 29.4 s", )
print("O resultado exato é {:.1f} s".format(v3))
