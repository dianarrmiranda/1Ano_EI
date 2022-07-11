#e) Se o volante for largado de uma altura de 20 m, quanto tempo demora a atingir o
#solo? Compare com o tempo que demoraria se não houvesse resistência do ar.
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

print('gt/vt= {:.3f}, tempo chegada ao solo (com resistência do ar)= {:.3f}s'.format(gt, t))

temlivre=np.sqrt(2*altura/g)
print('Tempo queda livre ao solo (sem resistência do ar)= {:.3f}s'.format(temlivre))
