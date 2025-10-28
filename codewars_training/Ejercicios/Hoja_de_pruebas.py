from operator import index

number = 31
numeros = list(range(3, int(number), 3))
numero2 = list(range(5, int(number), 5))
numer3=[]
print(numeros)
print(numero2 )
for numero in numeros:
    if numero in numero2:
        print ("numero repetido: "+ str(numero))
    else:
        numer3.append(numero)

print(numer3)

