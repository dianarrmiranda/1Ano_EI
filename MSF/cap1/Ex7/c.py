#c) Considerando a relação entre o período e a massa descoberta na alínea anterior,
#transforme as quantidades de modo a obter um gráfico que apresente uma relação linear.
#Encontre o declive, a ordenada na origem, os erros respetivos e o coeficiente de
#determinação. É um bom ajuste?


import numpy as np
import matplotlib.pyplot as plt

def regressaoLinear(x, y):
    npontos=x.size
    
    #b) Calcular somas

    sx = sum(x)
    sy= sum(y)
    sxy = 0
    for i in range(0,npontos):
        sxy += x[i]*y[i]
    sxx=sum([i**2 for i in x])
    syy=sum([i**2 for i in y])
    
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
    
    return m,dm,b,db,r2

M = np.array([0.15, 0.20,0.16,0.11,0.25,0.32,0.40,0.45,0.50,0.55])
T = np.array([1.21,1.40,1.26,1.05,1.60,1.78,2.00,2.11,2.22,2.33])

x = M
y = T

y_=[i**2 for i in y]

m = regressaoLinear(x, y_)[0]
b = regressaoLinear(x, y_)[2]

xmax=np.max(x)*0.9
xmin=np.min(x)*1.1
x1 = np.linspace(xmin, xmax, 100)

plt.plot(x,m*x+b)
plt.plot(x,y_, "ro")
plt.xlabel("M (Kg)")
plt.ylabel("T (s)")

m = regressaoLinear(x, y_)[0]
dm = regressaoLinear(x, y_)[1]
b = regressaoLinear(x, y_)[2]
db = regressaoLinear(x, y_)[3]
r2 = regressaoLinear(x, y_)[4]

print()
print("m +/-dm = {:0.8f} +/- {:0.8f}".format(m,dm))
print("b +/-db = {:0.8f} +/- {:0.8f}".format(b,db))
print("r2 = {:0.8f}".format(r2))

plt.show()
