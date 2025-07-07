

lista= [1,2,3,4]
print(max(lista))
diccionario= {"key1": 13, "key2" : 15, "key5": 25}

print(diccionario)


def devolver_distintos(**kwargs): 
    suma =0 
    lista=[]
    
    for key,value in kwargs.items():
        suma+= value
        lista.append(value)

    if suma > 15: 
        return max(kwargs.values())
    elif suma < 10 : 
        return min(kwargs.values())
    elif 15>=suma>=10:
        lista.remove(min(lista))
        lista.remove(max(lista))
        return lista[0]
    

print(devolver_distintos(num_1 = 0, num_2 =2, num_3 = 11))