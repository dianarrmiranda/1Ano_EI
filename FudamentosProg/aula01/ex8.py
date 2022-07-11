#Exercício 8 ficha 01

pf = 20

pc = 24.95

imp = pc * 0.23

spa = 0.20

lucro = ((pc-spa)/(1+imp))/pf

livros = input('Quantos Livros? ')

lucrolivros = livros*lucro

print('O Lucro com {} livros é de {}.'.format(livros, lucrolivros)

