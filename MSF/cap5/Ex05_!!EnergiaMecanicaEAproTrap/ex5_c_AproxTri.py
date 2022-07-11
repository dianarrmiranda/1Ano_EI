import matplotlib.pyplot as plt
import numpy as np

#c) Considerando a resistência do ar, calcule o trabalho realizado pela força de
#resistência do ar até às posições nos três instantes 𝑡0 = 0, 𝑡1 = 0.4 s e 𝑡2 = 0.8 s.
#Use a aproximação trapezoidal para calcular os integrais. A velocidade terminal da
#bola de ténis é 100 km/h. A bola de ténis tem a massa 57 g.

#trabalho realizado pela força de resistência do ar com Aproximação trapezoidal

v0 = 100/3.6 # m/s
teta = np.radians(10)
dt = 0.0001
g = 9.8
t0 = 0
tf =1
m = 0.057
vt = 100/3.6

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

vx = np.empty(n)
vy = np.empty(n)

vx[0] = v0*np.cos(teta)
vy[0] = v0*np.sin(teta)

ax = np.empty(n)
ay = np.empty(n)

x = np.empty(n) 
y = np.empty(n)

x[0] = 0
y[0] = 0

#Calcule a energia mecânica
v = np.empty(n)
Em = np.empty(n)
#-----------------

#Aceleração resistencia ar
aresx = np.empty(n)
aresy = np.empty(n)

#Integral aproximação trapezoidal
I = np.empty(n)
fun = np.empty(n) #função

#Cálculo resistência do ar
D = g/vt**2


for i in range(n-1):    
    v[i] = np.sqrt(vx[i]**2 + vy[i]**2)
    
    aresx[i] = -D*vx[i]*abs(v[i])
    ax[i] = aresx[i]
    aresy[i] = -D*abs(v[i])*vy[i]
    ay[i] =  aresy[i] - g 
    
    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] +ax[i]*dt
    
    y[i+1] = y[i] + vy[i] * dt
    x[i+1] = x[i] + vx[i] * dt
    
    Em[i] = 0.5*m*v[i]**2 + m*g*y[i]

    fun[i] = m*aresx[i]*vx[i]+m*aresy[i]*vy[i]
    I[i] = dt *((fun[0]+fun[i])*0.5 + np.sum(fun[1:n]))
    
    
#Para dar valor ao ultimo indice no array  
v[n-1] = np.sqrt(vx[n-1]**2 + vy[n-1]**2)
Em[n-1] = 0.5*m*v[n-1]**2 + m*g*y[n-1]

fun[n-1] = m*aresx[n-1]*vx[n-1]+m*aresy[n-1]*vy[n-1]
I[n-1] = dt *((fun[0]+fun[n-1])*0.5 + np.sum(fun[1:n]))
#------------------------------------------

for i in range(n-1):
    if (i==0):
        print("Integral[0] = {:0.2f} J".format(I[i]))
        plt.plot(t[i],I[i], "o", label="t=0")
    if (t[i] < 0.4 < t[i+1]):
        print("Integral[0.4] = {:0.2f} J".format( I[i]))
        plt.plot(t[i],I[i], "o", label="t=0.4")
    if (t[i] < 0.8 < t[i+1]):
        print("Integral[0.8] = {:0.2f} J".format( I[i]))
        plt.plot(t[i],I[i], "o", label="t=0.8")


plt.plot(t,I)
plt.title("Aproximação trapezoidal")
plt.legend()
plt.show()