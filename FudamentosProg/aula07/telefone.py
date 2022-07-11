# Complete este programa como pedido no guião da aula.

from os import name

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))

def filterPartName(contacts, partName):
    """Returns a new dict with the contacts whose names contain partName."""
    lista = {}
    for num, nome in contacts.items():
        if partName.lower() in nome.lower():
            lista[num] = nome
    return lista

def addLista(contactos):
    num = input("Número: ")
    if num in contactos:
        print("Este número já está nos contactos. Responda S para substituir o número atual")
        if input().upper() != "S":
            return None
    nome = input("Nome: ")
    contactos[num] = nome
    
    return print("Contacto adicionado")

def removeLista(contactos):
    num = input("Número: ")
    if num in contactos:  
        print("Apagar o número {} : {}? Introduza S para confirmar".format(num, contactos[num]))
        if input().upper() == "S":
            contactos.pop(num)
    else:
        print("Este número não pertence à lista")   
    return contactos     

def findNumLista(contactos):
    num = input("Número: ")
    print(contactos.get(num,num))
    
def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": "Universidade de Aveiro",
        "727392822": "Cristiano Aveiro",
        "387719992": "Maria Matos",
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
        "433162999": "Ana Bacalhau"
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "A":
            addLista(contactos)
        elif op == "R":
            removeLista(contactos)
        elif op == "N":
            findNumLista(contactos)
        elif op == "P":
            partName = input("Parte do nome: ")
            print()
            print("Correspondências:")
            listContacts(filterPartName(contactos, partName))        
        else:
            print("Não implementado!")
    

# O programa começa aqui
main()

