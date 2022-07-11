"""
Dada uma string, construa e devolva uma nova string onde
todas as letras 'x' apareçam movidas para o fim da string.
A função tem de ser recursiva. Não pode usar ciclos.

Given a string, return a new string where all the 
'x' chars have been moved to the end of the string.
The function must be recursive. You cannot use loops.

endX("xxre") → "rexx"
endX("xxhixx") → "hixxxx"
endX("hixhix") → "hihixx"
"""

def endX(s):
    if len(s) == 1: return s
    index = s.find('x')
    parteFinal = s[index:]
    xFinal = 'x' * len(parteFinal)
    if parteFinal == xFinal:
        return s
    return endX(s[0:index] + s[index+1:] + 'x')

print(endX('xxre'))

#Outra Solução

def movX2(s):
    sx=''.join([ch for ch in s if ch!='x'])
    return sx + (len(s)-len(sx))*'x'

print(movX2('xxre'))