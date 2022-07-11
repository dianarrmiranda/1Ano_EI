import numpy as np

#b) Calcular as somas das expressões do método dos mínimos quadráticos.

L=np.array([222.0,207.5,194,171.5,153.0,133.0,113.0,92.0])
X=np.array([2.3,2.2,2.0,1.8,1.6,1.4,1.2,1.0])

#Truque para não ter de alterar o código abaixo: identificar x e y corretamente
x=L
y=X

npontos=x.size

#b) Calcular somas

xy=x*y # element by element product
x2=x*x
y2=y*y

sx=x.sum()
sy=y.sum()
sxy=xy.sum()
sxx=x2.sum()
syy=y2.sum()

print("{:13}{:13}{:13}{:13}{:13}".format("Soma do x","Soma do y","Soma do x*y", "Soma de x**2", "Soma de y**2"))
print("{:<13}{:<13}{:<13}{:<13}{:<13}".format(sx,sy,sxy,sxx,syy))