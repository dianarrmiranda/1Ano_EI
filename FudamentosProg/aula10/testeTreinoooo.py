import imp
from operator import le
from re import X


peso = float(input("Peso (kg)? "))
altura = float(input("Altura (m)? "))

imc = peso / altura**2

print("O adulto tem um IMC de {0:.1f}".format(imc))

if imc < 18.5:
    print("Baixo peso")
elif 18.5 <= imc <= 25:
    print("Normal")
else:
    print("Obesidade")

#2

def IMC(peso, altura):
    imc = peso / altura**2
    
    return imc

def classificacao(imc):
    x=''
    if imc < 18.5:
        x =  "Baixo peso"
    elif 18.5 <= imc <= 25:
        x = "Normal"
    else:
        x = "Obesidade"
    return x

def lerValorPositivo(text):
    n = float(input(text))
    while n < 0.0:
        n = float(input('Número inválido! ' + text))
    return n

def menu():
    print('  ')
    print('  ')
    print('Opções disponíveis:')
    print('0 - sair')
    print('1 - introduzir nova medida')
    print('2 - mostrar média atual')
    return int(input('Opção? '))

print('Bem vindo(a) à calculadora do IMC')


somaimc=0
n=0

while True:
    op = menu()
    if op == 0:
        print('FIM')
        print('Até breve')
        break
    elif op ==1:
        peso = lerValorPositivo("Peso (kg)? ")
        altura = lerValorPositivo("Altura (m)? ")
        imc = IMC(peso,altura)
        print("O adulto tem um IMC de {0:.1f}".format(imc))
        print(classificacao(imc))
        somaimc += imc
        n+=1
    elif op == 2:
        print('Estatísticas atuais:')
        if n == 0:
            print('Ainda não foram efetuados cálculos!')
        else:
            print('Valor médio do IMC para {} adultos: {:0.2f}'.format(n,somaimc/n))
    else:
        print('Opção Inválida!')
        
    

