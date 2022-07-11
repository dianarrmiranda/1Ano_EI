#Calcular Potência

u = 0.004 
m = 1200 #kg
Area = 3 #m
par = 1.225
g=9.8
Cres = 0.9

v = 90/3.6
vx = 90/3.6

Fres = (Cres*Area*par*v**2*vx)/2

P = u*m*g*v + Fres

print("Potência a 90 km/h: {:.0f} W = {:.0f} CV".format(P, P/735.499))

v = 130/3.6
vx = 130/3.6

Fres = (Cres*Area*par*v**2*vx)/2

P = u*m*g*v + Fres

print("Potência a 130 km/h: {:.0f} W = {:.0f} CV".format(P, P/735.499))