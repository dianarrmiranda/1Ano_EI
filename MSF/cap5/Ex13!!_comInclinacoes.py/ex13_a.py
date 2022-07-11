import matplotlib.pyplot as plt
import numpy as np

#a) Quanto tempo demora a percorrer 2 km?

u = 0.004  #coeficiente de resistência u
m = 75 #massa
Area = 0.3
par = 1.225 #densidade
g=9.8 #gravidade
Cres = 0.9 #coefeciente da resistência do ar

teta = np.radians(5)

P = 0.4*735.49875 #potencia

t0 = 0
tf =50.00
dt = 0.001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

fAtrito=-u*m*g*np.cos(teta)
#fAtrito=-mu*massa*g #segundo sugetsoa do Torres. Ver apontamentos

vx = np.empty(n)
v = np.empty(n)
ax = np.empty(n)
x = np.empty(n)

aresx=np.empty(n)
fcil=np.empty(n)

vx[0] = 1
x[0] = 0

tolerancia=0.00000000000001

pesoX=-m*g*np.sin(teta)


for i in range(n-1):   
    
    v[i] = np.sqrt(vx[i]**2)
    aresx[i] = -Cres/(2*m)*Area*par*v[i]*vx[i]
    fcil[i] = P/(m*v[i])
    ax[i+1] = fAtrito/m+aresx[i]+fcil[i]+pesoX/m
    vx[i+1] = vx[i] +ax[i]*dt
    x[i+1] = x[i] + vx[i] * dt
    
v[n-1] = np.sqrt(vx[n-1]**2)

for i in range(n-1):
    if (t[i]>48-tolerancia and t[i]>48+tolerancia ): 
        print("velocidade terminal = {:0.2f} m/s".format( v[i]))
        plt.plot(t[i],v[i], "o", label="velociade terminal")
        break

    
plt.plot(t,v)
plt.xlabel("t (s)")
plt.ylabel("v (m/s)")
plt.title("Velocidade Terminal")
plt.show()
