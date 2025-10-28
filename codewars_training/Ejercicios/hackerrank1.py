import math

def sockMerchant(n, ar):
    """
    dado n es el número del tamaño del array
    ar es un array donde cada número representa un color
    n : int 
    ar : list
    
    return : 
    regresa un int con el numero de pares del mismo color que hay 
    """
    #Variables


    colores = set()
    cantidad_por_color = {}
    total_pares = 0
    for color in ar: 
        if color not in colores: 
            cantidad_pares_color = math.floor(ar.count(color)/2)
            colores.add(color)
            cantidad_por_color[color] = cantidad_pares_color
            total_pares += cantidad_pares_color
   
    return total_pares



n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]


print(sockMerchant(n,ar))

print(type(sockMerchant(n,ar)))