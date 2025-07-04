palabra  = "Python"

lista = []

for letra in palabra: 
 lista.append(letra)
print(lista)

# es equivalente a 

lista2 = [letra for letra in "Python"]

print(lista2)


lista3 = [numero if numero*2 > 10 else "no" for numero in range(0,21,2) ] 
print(lista3)



pies = [10,20,30,40,50]

metros = [p/3.281 for p in pies]

print(metros)


valores = [1, 2, 3, 4, 5, 6, 9.5] 

valores_pares = [valor for valor in valores  if valor%2==0 ]
print( valores_pares)