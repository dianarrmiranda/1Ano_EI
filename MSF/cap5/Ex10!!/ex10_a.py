#Calcular Potência

u = 0.004
m = 75
Area = 0.3
par = 1.225
v = 40/3.6
g=9.8
Cres = 0.9
vx = 40/3.6

Fres = (Cres*Area*par*v**2*vx)/2

P = u*m*g*v + Fres

print("Potência a 40 km/h do ciclista da frente: {:.0f} W".format(P))

total = P
Area = 0.21

Fres = (Cres*Area*par*v**2*vx)/2

P = u*m*g*v + Fres

print("Potência a 40 km/h de um ciclista do pelotão: {:.0f} W".format(P))
print("Potência a 40 km/h total: {:.0f} W".format(total+P))