#f) Nas condições da alínea anterior, qual o valor da velocidade e da aceleração quando
#o volante chega ao solo?

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym #calculo simbólico

altura=20.0
g = 9.80 #gravidade
vt = 6.80

# alinea e) 
ext=altura*g/vt**2
ex=np.exp(ext)
gt=np.arccosh(ex)
t=gt*vt/g

# alinea  f)

veloc=vt*np.tanh(g*t/vt)
print('Velocidade(solo) = {:.3f} m/s'.format(veloc))

acele=g/np.cosh(g*t/vt)**2
print('Aceleração (solo) = {:.3f} m/s^2'.format(acele))
