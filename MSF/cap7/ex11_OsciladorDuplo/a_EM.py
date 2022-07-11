import matplotlib.pyplot as plt
import numpy as np

#c) Qual a sua energia mecânica?

m = 1
k = 1

xeq =2

x0 = 3 
v0 = 0


t0 = 0
tf =30
dt = 0.001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)

em=np.zeros(n)


x[0] = x0
v[0] = v0

em[0]= 0.5*(np.abs(x[0])-xeq)**2*m + 0.5* v[0]**2*m

a[0] = -x[0] + xeq

for i in range(n-1):  
    if x[i]<0:
        a[i+1] = (-x[i+1] - xeq)/m
    if x[i]>0:
        a[i+1] = (-x[i+1] + xeq)/m
    v[i+1] = v[i] +a[i+1]*dt #a[i+1] - euler cromer
    x[i+1] = x[i] +v[i+1]*dt
    
    em[i]=  0.5*(np.abs(x[i])- xeq)**2*m + 0.5*v[i]**2*m

em[n-1]=  0.5*(np.abs(x[n-1])- xeq)**2*m + 0.5*v[n-1]**2*m

print("-----------------Alinea (a)-------------------")
print(em[0],"J (joules)")

