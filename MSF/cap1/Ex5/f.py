#f) Afaste da reta encontrada um dos valores medidos de 𝑋. Compare o coeficiente de
#determinação com o valor anterior. Faça um gráfico com os novos pontos experimentais
#e a nova reta.

from distutils.util import run_2to3
import numpy as np
import matplotlib.pyplot as plt

#Função da regressão linear
def regressaoLinear(x, y):
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
    
    return m,b, r2

#f) Afaste da reta encontrada um dos valores medidos de 𝑦. Compare o coeficiente de determinação com o valor anterior. 
# Faça um gráfico com os novos pontos experimentais e a nova reta.

#-----------------------ORIGINAL---------------------------------#
L=np.array([222.0,207.5,194,171.5,153.0,133.0,113.0,92.0])
X=np.array([2.3,2.2,2.0,1.8,1.6,1.4,1.2,1.0])
           
#Truque para não ter de alterar o código abaixo: identificar x e y corretamente
x=L
y=X

resultado_regrassao = regressaoLinear(x, y)
m = resultado_regrassao[0]
b = resultado_regrassao[1]

#d) Fazer um gráfico com os pontos experimentais e a reta cujos parâmetros m e b 

x_g = np.arange(80, 240, 10) #(y,x,numero de pontos)
  
l_g = m*x_g + b #Equação da reta y = mx + b

#Invocar gráfico
plt.scatter(L,X)
plt.xlabel("L (cm)")
plt.ylabel("X (cm)")

#-----------------------MODIFICADO---------------------------------#
y = np.array([2.3,2.2,2.0,2.1,1.6,1.4,1.2,1.0])

resultado_regrassao = regressaoLinear(x, y)
m = resultado_regrassao[0]
b = resultado_regrassao[1]
r2 = resultado_regrassao[2]

x_g = np.arange(80, 240, 10) #(y,x,numero de pontos)
l_g_new = m*x_g + b #Equação da nova reta y = mx + b

print("r^2 = ", r2)
#Invocar gráfico
plt.scatter(L,y)
plt.plot(x_g, l_g, '--', label = "Ajuste com os pontos originais") 
plt.plot(x_g, l_g_new, '--',label = "Ajuste com os pontos modificados") 
plt.legend()
plt.show()