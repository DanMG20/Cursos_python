lista_numeros = [-1,2,-3]
def todos_positivos(lista_numeros):
    
    for n in lista_numeros: 
        if n<0: 
            return False
        else: 
            pass
    return True

print(todos_positivos(lista_numeros))


def suma_menores(lista_numeros):
    for n in lista_numeros: 
        if 1000>n>0: 
            suma = suma + n 
        else:
            pass
    return suma 
lista_numeros1 = list(range(1,15))
print (lista_numeros1)
def cantidad_pares(lista_numeros):
    contador_pares = 0 
    for n in lista_numeros:
        if n%2==0: 
            contador_pares +=1
        else:
            pass
    return contador_pares
