#b) Apresente as medições num gráfico log-log. Qual a dependência entre as quantidade
#energia emitida e a temperatura? 

import numpy as np
import matplotlib.pyplot as plt

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
    
    return m, dm, b, db, r2


T= [200, 300 , 400, 500, 600, 700, 800, 900, 1000, 1100]
E = [0.6950, 4.363, 15.53, 38.74, 75.08, 125.2, 257.9, 344.1, 557, 690.7]

x=T
y=E

logx= np.log(T)
logy=np.log(E)
xmax=np.max(logx)*1.1
xmin=np.min(logx)*0.9

x = np.linspace(xmin, xmax, 100)#Gerar array com 100 valores
m= regressaoLinear(logx, logy)[0]
dm = regressaoLinear(logx, logy)[1]
b=regressaoLinear(logx, logy)[2]
db = regressaoLinear(logx, logy)[3]
r2 = regressaoLinear(logx, logy)[4]

print()
print("m +/-dm = {:0.8f} +/- {:0.8f}".format(m,dm))
print("b +/-db = {:0.8f} +/- {:0.8f}".format(b,db))
print("r2 = {:0.8f}".format(r2))

plt.plot(x,m*x+b)
plt.plot(logx, logy, "ro")
plt.show()

#A dependencia entre as quantidades de energia emitida e a temperatude é o valor de
# m +/- dm e r2