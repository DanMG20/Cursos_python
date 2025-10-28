"""

Normalmente, al comprar algo, te preguntan si tu número de tarjeta de crédito, 
número de teléfono o la respuesta a tu pregunta más secreta siguen siendo correctos. 
Sin embargo, como alguien podría mirar por encima de tu hombro, 
no quieres que eso se muestre en tu pantalla. En su lugar, lo ocultamos.
Tu tarea es escribir una función "maskify", 
que cambia todos los caracteres excepto los últimos cuatro a "#"."""


cc= "12389439184892"
# return masked string
def maskify(cc):
    final=""
    #1 contar caracteres 
    longitud =len(cc)
    #2 cambiar todos los caracteres hasta que solo queden 4 
    inicio = "#"*(longitud-4)

    for indice, letra in enumerate(cc): 
        if indice>=(longitud-4):
            final +=letra
    
    return inicio+final


print(maskify(cc))