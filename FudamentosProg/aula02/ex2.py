
#Exercício 2 ficha 02

# coding: utf-8
# This program finds the maximum of two numbers.
# It uses the built-in max function.
# Can you do it with conditional statements (if / if-else) instead?

x1 = float(input("number? "))
x2 = float(input("number? "))

# Use conditional statements instead of max function!
if x1 > x2:
    m = x1
else:
    m = x2

print('Máximo: {}'.format(m))

