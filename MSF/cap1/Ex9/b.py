#b) Apresente as medições num gráfico semilog. Como depende a atividade com o tempo?
#A unidade curie indica 3,7 × 1010 desintegrações nucleares/s

import matplotlib.pyplot as plt
import numpy as np

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

R = [9.676 , 6.355, 4.261, 2.729, 1.862, 1.184, 0.7680, 0.4883, 0.3461, 0.2119]
t = np.array([0,5,10,15,20,25,30,35,40,45])

x = t
y = R

logy = np.log(y)
plt.plot(x,logy,"o")

m = np.polyfit(x,logy,1)[0]
b = np.polyfit(x,logy,1)[1]

dm = regressaoLinear(x, logy)[1]

x = np.linspace(0, 50 * 1.1, 10000)

# A relação é linear
print("m +/-dm = {:0.8f} +/- {:0.8f}".format(m,dm))

plt.plot(x, m*x+b)
plt.xlabel("Tempo (dias)")
plt.ylabel("log da Radioatividade (mCi)")
plt.show()
