
import matplotlib.pyplot as plt
import numpy as np

#c) Calcule numericamente a lei do movimento, no caso em que a velocidade inicial é
#-3 m/s e a posição inicial -4 m..

m = 1
k = 1
g=9.8

b=0.05 #kg
f=7.5 #N
wf=2 #rad/s

print("Frenquencia Angular {:.4f} rad/s".format(np.sqrt(k/m - (b/(2*m))**2)))


