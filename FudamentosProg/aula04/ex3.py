#Exercício 03 ficha 04

# This program generates 20 terms of a sequence by a recurrence relation.
Un = 100                    # Un = each term of the sequence. Initially = U0
n = 0
while Un > 0:
    print(Un)
    Un = 1.01*Un - 1.01
    n +=1

print("Mostrou {} termos.".format(n))

    
#for n in range(20):
    #print(Un)
    #Un = 1.01*Un - 1.01     # Set Un to the next term of the sequence
