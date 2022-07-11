#Exercício 11 ficha 04

n = int(input('Número: '))
divisores =0
conta = 0

if n<0:
    print('Erro! Insira um número positivo.')
    n = int(input('Novo número: '))

for i in range(1, n):
    if n % i == 0:
        divisores += 1
        conta +=i

print('O número {} tem {} divisores.'.format(n,divisores))

if conta < n:
    print('{} é um número deficiente'.format(n))
elif conta == n:
     print('{} é um número perfeito'.format(n))
else:
    print('{} é um número abundante'.format(n))