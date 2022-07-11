# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {:^25} : {:<12}".format("Numero", "Nome", "Morada"))
    for num in dic:
        print("{:>12s} : {:^25} : {:<12}".format(num, dic[num][0], dic[num][1]))

def filterPartName(contacts, partName):
    list = {}
    for i in contacts:
        name = contacts[i][0]
        partName = partName.lower()
        name = name.lower()
        if partName in name:
            list[i] = contacts[i]
    return list

def filterPartMorada(contacts, partMor):
    list = {}
    for i in contacts:
        morada = contacts[i][1]
        morada=morada.lower()
        partMor = partMor.lower()
        
        if partMor in morada:
            list[i] = (contacts[i][0],contacts[i][1])
    return list
        

def addLista(contactos):
    nome = input('Nome: ')
    num = input('Número: ')
    morada = input('Morada: ')
    contactos[num] = (nome,morada)

def removeLista(contactos):
    num = input('Número: ')
    if num in contactos:
        contactos.pop(num)

def findNumLista(contactos):
    num = input('Número: ')
    print(contactos.get(num,num))
    
def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("Procurar parte da (M)orada")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": ("Universidade de Aveiro", "Santiago, Aveiro"),
        "727392822": ("Cristiano Aveiro", "Santarem"),
        "387719992": ("Maria Matos", "Porto"),
        "887555987": ("Marta Maia", "Porto"),
        "876111333": ("Carlos Martins", "Coimbra"),
        "433162999": ("Ana Bacalhau", "Lisboa")
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
        elif op == "M":
            partMor = input("Parte da morada: ")
            print()
            print("Correspondências:")
            listContacts(filterPartMorada(contactos, partMor))        
        else:
            print("Não implementado!")
    

# O programa começa aqui
main()

