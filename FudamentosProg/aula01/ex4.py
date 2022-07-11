#Exercício 4 ficha 01

tempo = int(input('Tempo em segundos: '))

h = tempo // 3600

segundos_rest = tempo % 3600

m = segundos_rest //60

s = segundos_rest % 60

print('{:02d}:{:02d}:{:02d}'.format(h,m,s))
