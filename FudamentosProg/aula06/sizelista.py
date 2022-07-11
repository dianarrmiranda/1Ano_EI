#Exercício 7 ficha 06

import os

def SizeLista(dir_pasta="./"):
    print("{:60}{:>10}".format("File", "Size"))
    for f in os.listdir(dir_pasta):
        print("{:60}{:10}".format(f, os.stat(f).st_size))

SizeLista()