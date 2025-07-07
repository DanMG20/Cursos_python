#Debe identificar todos los numeros primos
def contar_primos(numero_tope):
    primos = [2]
    iteracion =  3

    if numero_tope<2: 
        return 0 
    while iteracion <= numero_tope : 
        for n in range(3,iteracion,2): 
            if iteracion % n == 0: 
                iteracion +=2
                break
        else:
            primos.append(iteracion)
            iteracion +=2 
    print(primos)
    return len(primos)

contar_primos(3)
