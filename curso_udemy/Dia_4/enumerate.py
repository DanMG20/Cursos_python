# para sacar indices de una coleccion 
# como en una lista 


lista = ["a","b","c"]
indice = 0 


for item in lista: 
    print(indice,item)
    indice +=1


#es equivalente a:


for indice, item in enumerate(lista): 
    print(indice,item)



# para comvertir a tuplas indizadas 

tuplas = list(enumerate(lista))
print(tuplas)