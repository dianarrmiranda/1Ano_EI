#Calcular Potência

u = 0.004
m = 75
Area = 0.3
par = 1.225
v = 30/3.6
g=9.8
Cres = 0.9
vx = 30/3.6

Fres = (Cres*Area*par*v**2*vx)/2

P = u*m*g*v + Fres

print("Potência a 30 km/h: {:.0f} W = {:.3f} cv".format(P, P/735.4975))

v = 40/3.6

vx = 40/3.6

Fres = (Cres*Area*par*v**2*vx)/2

P = u*m*g*v + Fres

print("Potência a 40 km/h: {:.0f} W = {:.3f} cv".format(P,P/735.4975))

v = 296.010/3.6

vx = 296.010/3.6

Fres = (Cres*Area*par*v**2*vx)/2

P = u*m*g*v + Fres

print("Potência a 296.010 km/h: {:.0f} W = {:.3f} cv".format(P,P/735.4975))
