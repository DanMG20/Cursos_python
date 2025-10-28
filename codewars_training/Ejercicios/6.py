"""
Implemente la función unique_in_order, que toma como argumento una secuencia y 
devuelve una lista de elementos sin elementos con el mismo valor adyacentes,
 conservando el orden original de los elementos.
"""

"""
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']



1.-Borrar datos repetidos 
2.-Agregarlos en el mismo orden
"""
cadena='AAAABBBBASSSSSS'

def unique_in_order(cadena): 
    caracteres = []
    longitud_cadena = len(cadena)
    print(longitud_cadena)
    for indice,caracter in enumerate(cadena): 
 
        if indice+1 == longitud_cadena:
            print('anterior')
            print( cadena[indice-1])
            print("actual")
            print(caracter) 
        elif cadena[indice+1] !=caracter:
            caracteres.append(caracter)
    return caracteres
        
    
print(unique_in_order(cadena))

