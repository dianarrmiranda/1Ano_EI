#Exercício 5 ficha 02

litros = float(input('Quantidade de litros? '))

if litros <= 40:
    custo = litros * 1.40
else: 
    custo = (litros*1.40)*0.9

print(custo)
