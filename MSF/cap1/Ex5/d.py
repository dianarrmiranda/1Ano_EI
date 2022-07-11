import numpy as np
import matplotlib.pyplot as plt

#d) faça um gráfico com os pontos experimentais e a reta cujos parâmetros m e b calculou
#anteriormente

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

#c) Calcular o declive, a ordenada na origem e o coeficiente de determinação ou de correlação 𝑟**2
n=npontos
rn=n*sxy-sx*sy
rd=(n*sxx-sx**2)*(n*syy-sy**2)
r2=rn**2/rd
r=np.sqrt(r2)
m=(n*sxy-sx*sy)/(n*sxx-sx**2)
dm=abs(m)*np.sqrt((1/r**2-1)/(n-2))
bn=sxx*sy-sx*sxy  
bd=n*sxx-sx**2
b=bn/bd
db=dm*np.sqrt(sxx/n)

#d) Fazer um gráfico com os pontos experimentais e a reta cujos parâmetros m e b 

x_g = np.arange(80, 240, 10) #(y,x,numero de pontos)
  
l_g = m*x_g + b #Equação da reta y = mx + b

#Invocar gráfico
plt.scatter(L,X) #(x,y)
plt.xlabel("L (cm)")
plt.ylabel("X (cm)")
plt.plot(x_g, l_g, '--')

plt.show()
